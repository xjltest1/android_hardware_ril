/* //device/system/rild/rild.c
**
** Copyright 2006, The Android Open Source Project
** Copyright (c) 2010-2012, Code Aurora Forum. All rights reserved.
**
** Licensed under the Apache License, Version 2.0 (the "License");
** you may not use this file except in compliance with the License.
** You may obtain a copy of the License at
**
**     http://www.apache.org/licenses/LICENSE-2.0
**
** Unless required by applicable law or agreed to in writing, software
** distributed under the License is distributed on an "AS IS" BASIS,
** WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
** See the License for the specific language governing permissions and
** limitations under the License.
*/

#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

#include <telephony/ril.h>
#define LOG_TAG "RILD"
#include <utils/Log.h>
#include <cutils/properties.h>
#include <cutils/sockets.h>
#include <linux/capability.h>
#include <linux/prctl.h>

#include <private/android_filesystem_config.h>
#include "hardware/qemu_pipe.h"
#include <pthread.h>

#include <termios.h>


#define LIB_PATH_PROPERTY   "rild.libpath"
#define LIB_ARGS_PROPERTY   "rild.libargs"
#define MAX_LIB_ARGS        16
#define NUM_CLIENTS 	    2

#define DSDARILPATH           "/system/lib/libscril.so"
#define DSDARILPATH0           "/system/lib/libscril0.so"


const RIL_RadioFunctions *funcs_inst_for_sim0[NUM_CLIENTS] = {NULL, NULL};
const RIL_RadioFunctions *funcs_inst[NUM_CLIENTS] = {NULL, NULL};
static int last_switch_state = 0;

static void usage(const char *argv0)
{
    fprintf(stderr, "Usage: %s -l <ril impl library> [-- <args for impl library>]\n", argv0);
    exit(-1);
}

extern void RIL_register (const RIL_RadioFunctions *callbacks, int client_id);

extern void RIL_onRequestComplete(RIL_Token t, RIL_Errno e,
                           void *response, size_t responselen);
//In case of DSDS two unsol functions are needed, corresponding to each of the commands interface.
extern void RIL_onUnsolicitedResponse(int unsolResponse, const void *data,
                                size_t datalen);

extern void RIL_requestTimedCallback (RIL_TimedCallback callback,
                               void *param, const struct timeval *relativeTime);
extern void RIL_setMaxNumClients(int num_clients);

static int isMultiSimEnabled();
static int isMultiRild();
static struct RIL_Env s_rilEnv = {
    RIL_onRequestComplete,
    RIL_onUnsolicitedResponse,
    RIL_requestTimedCallback
};
static struct RIL_Env s_rilEnv2 = {
    RIL_onRequestComplete,
    RIL_onUnsolicitedResponse2,
    RIL_requestTimedCallback
};

extern void RIL_startEventLoop();

static int make_argv(char * args, char ** argv)
{
    // Note: reserve argv[0]
    int count = 1;
    char * tok;
    char * s = args;

    while ((tok = strtok(s, " \0"))) {
        argv[count] = tok;
        s = NULL;
        count++;
    }
    return count;
}

/*
 * switchUser - Switches UID to radio, preserving CAP_NET_ADMIN capabilities.
 * Our group, cache, was set by init.
 */
void switchUser() {
    prctl(PR_SET_KEEPCAPS, 1, 0, 0, 0);
    setuid(AID_RADIO);

    struct __user_cap_header_struct header;
    struct __user_cap_data_struct cap;
    header.version = _LINUX_CAPABILITY_VERSION;
    header.pid = 0;
    cap.effective = cap.permitted = (1 << CAP_NET_ADMIN) | (1 << CAP_NET_RAW);
    cap.inheritable = 0;
    capset(&header, &cap);
}

#if 0  // for SKU2, not for SKU1
//add for switching sim1 between CDMA and GSM
void *thread_function(void *arg)
{
    char switch_state[10]= {0};
    //char old_switch_state[10]= {0};
reset:
    while(1){
        property_get("gsm.switch.cdma",switch_state,"0");
        //property_get("gsm.switch.oldstate",old_switch_state,"0");
        //if(('1' == switch_state[0]) && ('0' == old_switch_state[0])){
        if(('1' == switch_state[0]) && (0 == last_switch_state)){
            //switch sim0 from MSM8625 to SC6610
            last_switch_state = 1;
            //property_set("gsm.switch.oldstate","1");
            ALOGE("Register the callbacks func for switching sim0 from MSM8625 to SC6610");
            system("echo GSM > /sys/class/switch/sim-slot/switch");
            RIL_setcallbacks(funcs_inst_for_sim0[0], 0);
        }else if(('0' == switch_state[0]) && (1 == last_switch_state)){
            //switch sim1 from SC6610 to MSM8625
            last_switch_state = 0;
            system("echo CDMA > /sys/class/switch/sim-slot/switch");
            ALOGE("Register the callbacks func for switching sim0 from SC6610 to MSM8625");
            RIL_setcallbacks(funcs_inst[0], 0);
        }
        sleep(2);
    }
    return NULL;
}
#endif

#if 1  // for mux
/*
* Purpose:  Open and initialize the serial device used.
* Input:      serial - the serial struct
* Return:    0 if port successfully opened, else 1.
*/
int open_serial_device(const char* 	devicename, speed_t speed)
{
  int file_ptr = 0;

	struct termios options;

	ALOGE("open_serial_device Enter");

	file_ptr = open(devicename, O_RDWR | O_NOCTTY | O_NDELAY);
	//file_ptr = open("/dev/ttyMSMSKU92", O_RDWR | O_NOCTTY | O_NDELAY);
	if (-1 == file_ptr) {
		printf("Could not open uart port \n");
		return(-1);
	}

	ioctl(file_ptr, TCGETS, &options);
	options.c_cc[VTIME]    = 0;   /* inter-character timer unused */
	options.c_cc[VMIN]     = 2;   /* blocking read until 5 chars received */

	options.c_cflag &= ~CSIZE;
	options.c_cflag |= (CS8 | CLOCAL | CREAD |CRTSCTS);
	options.c_iflag = IGNPAR;
        options.c_oflag = 0;
	options.c_lflag = 0;

	cfsetospeed(&options, speed);
	cfsetispeed(&options, speed);
	ioctl(file_ptr, TCSETS, &options);

		/* Blocking behavior */
	fcntl(file_ptr, F_SETFL, 0);

#if 0
  /* open the serial port */
	if ((fd = open(devicename, O_RDWR | O_NOCTTY | O_NONBLOCK)) < 0)
  {
    ALOGE("open_serial_device F1 %s [%d]", strerror(errno), errno);
    return -1;
  }

	ALOGE("Opened serial port");

	int fdflags;
	if ((fdflags = fcntl(fd, F_GETFL)) < 0)
  {
    ALOGE("open_serial_device F2 %s [%d]", strerror(errno), errno);
    return -1;
  }
	if (fcntl(fd, F_SETFL, fdflags & ~O_NONBLOCK) < 0)
  {
    ALOGE("open_serial_device F2 %s [%d]", strerror(errno), errno);
    return -1;
  }

	struct termios t;
  tcgetattr(fd, &t);

  t.c_cc[VTIME]    = 0;
	t.c_cc[VMIN]     = 0;

	t.c_cflag &= ~CSIZE;
	t.c_cflag |= (CS8 | CLOCAL | CREAD);
	t.c_cflag &=~PARENB;
	t.c_cflag |= CRTSCTS;
	t.c_iflag = IGNPAR;
        t.c_oflag = 0;
	t.c_lflag = 0;

	//Android does not directly define _POSIX_VDISABLE. It can be fetched using pathconf()
	long posix_vdisable;
	char cur_path[FILENAME_MAX];
	if (!getcwd(cur_path, sizeof(cur_path))){
		ALOGE("_getcwd returned error: %s [%d]", strerror(errno), errno);
		return 1;
	}
	posix_vdisable = pathconf(cur_path, _PC_VDISABLE);
	t.c_cc[VINTR] = posix_vdisable;
	t.c_cc[VQUIT] = posix_vdisable;
	t.c_cc[VSTART] = posix_vdisable;
	t.c_cc[VSTOP] = posix_vdisable;
	t.c_cc[VSUSP] = posix_vdisable;

	speed_t speed = B115200;
	cfsetispeed(&t, speed);
	cfsetospeed(&t, speed);

  ioctl(fd, TCSETS, &t);
#endif

	ALOGE("Configured serial device");

	return file_ptr;
}

#if 0
/*
* Purpose:  Compares two strings.
*                strstr might not work because WebBox sends garbage before the first OK
*                when it's not needed anymore
* Input:      haystack - string to check
*                length - length of string to check
*                needle - reference string to compare to. must be null-terminated.
* Return:    1 if comparison was success, else 0
*/
static int memstr(
	const char *haystack,
	int length,
	const char *needle)
{
	int i;
	int j = 0;
	if (needle[0] == '\0')
		return 1;
	for (i = 0; i < length; i++)
		if (needle[j] == haystack[i])
		{
			j++;
			if (needle[j] == '\0') // Entire needle was found
				return 1;
		}
		else
			j = 0;
	return 0;
}

/*
* Purpose:  Sends an AT-command to a given serial port and waits for reply.
* Input:      fd - file descriptor
*                cmd - command
*                to - how many seconds to wait for response
* Return:   0 on success (OK-response), -1 otherwise
*/
static int chat(
	int serial_device_fd,
	const char *cmd,
	int to)
{
	ALOGE("chat Enter");
	unsigned char buf[1024];
	int sel;
	int len;
	int wrote = 0;
	ALOGE(">s %s", cmd);
	if ((wrote = write(serial_device_fd, cmd, strlen(cmd))) < 0)
  {
    ALOGE("chat F1 %s [%d]", strerror(errno), errno);
    return -1;
  }
	ALOGE("Wrote %d bytes", wrote);

  ioctl(serial_device_fd, TCSBRK, 1); //equivalent to tcdrain for andriod

	fd_set rfds;
	FD_ZERO(&rfds);
	FD_SET(serial_device_fd, &rfds);
	struct timeval timeout;
	timeout.tv_sec = to;
	timeout.tv_usec = 0;
	do
	{
		if ((sel = select(serial_device_fd + 1, &rfds, NULL, NULL, &timeout)) < 0)
    {
      ALOGE("chat F2 %s [%d]", strerror(errno), errno);
      return -1;
    }
		ALOGE("Selected %d", sel);
		if (FD_ISSET(serial_device_fd, &rfds))
		{
			memset(buf, 0, sizeof(buf));
			if ((len = read(serial_device_fd, buf, sizeof(buf))) < 0)
      {
        ALOGE("chat F3 %s [%d]", strerror(errno), errno);
        return -1;
      }

      ALOGE("Read %d bytes from serial device", len);
      unsigned char tmpc = buf[len];
      buf[len] = '\0';
			ALOGE("<s %s", buf);
      buf[len] = tmpc;
			errno = 0;
			if (memstr((char *) buf, len, "OK"))
			{
				ALOGE("Received OK");
				return 0;
			}
			if (memstr((char *) buf, len, "ERROR"))
			{
				ALOGE("Received ERROR");
				return -1;
			}
		}
	} while (sel);
	return -1;
}
#endif

static void *
openSerial(void *param){
    int try_times = 10;
    int fd = 0;
    FILE *fp;
    char platform_version[8];

    fp = fopen("/sys/devices/system/soc/soc0/platform_version", "r");
    if(!fp)
    {
      ALOGE("MUXTest Opened serial: read config file failed.");
    }

    if (fp && fgets(platform_version, sizeof(platform_version), fp) && !strncmp(platform_version, "131072", 6))
    {
        ALOGE("MUXTest Opened serial: /dev/ttyMSM2");
        fd = open_serial_device("/dev/ttyMSM2", B115200);
    }
    else
    {
        ALOGE("MUXTest Opened serial: /dev/ttyHSL0");
        fd = open_serial_device("/dev/ttyHSL0", B460800);
    }
    ALOGE("MUXTest Opened serial dev.%d", fd);
    fclose(fp);

#if 0
    ALOGE("MUXTest Chat.");
    while (chat(fd, "AT\r\n", 1) < 0)
    {
      if (!(--try_times)) {
        ALOGE("Modem does not respond to AT commands in 10 times, trying close mux mode");
        break;
      }
      //LOGE("Modem does not respond to AT commands in 2 seconds, sleep 1 second and trying again.");
      //sleep(1);
    }
#endif
    return NULL;
}
#endif

int main(int argc, char **argv)
{
    const char * rilLibPath = NULL;
    char **rilArgv;
    static char * s_argv[MAX_LIB_ARGS];
    void *dlHandle;
    void *simdlHandle;
    const RIL_RadioFunctions *(*rilInit)(const struct RIL_Env *, int, char **);
    const RIL_RadioFunctions *(*DSDARILInit)(const struct RIL_Env *, int, char **); 
    char libPath[PROPERTY_VALUE_MAX];
    unsigned char hasLibArgs = 0;
    int j = 0;
    int i;
    static char client[3] = {'0'};
    int numClients = 1;

#if 0 //for SKU2, not for SKU1
    //add for switching sim0 between CDMA and GSM
    void *simdlHandle_for_sim0;
    const RIL_RadioFunctions *(*DSDARILInit_for_sim0)(const struct RIL_Env *, int, char **);
    pthread_t a_thread;
    int res;
#endif

    ALOGE("**RIL Daemon Started**");
    ALOGE("**RILd param count=%d**", argc);
    memset(s_argv, 0, MAX_LIB_ARGS*sizeof(char));

    s_argv[0] = argv[0];
    umask(S_IRGRP | S_IWGRP | S_IXGRP | S_IROTH | S_IWOTH | S_IXOTH);
    for (i = 1, j = 1; i < argc ;) {
        if (0 == strcmp(argv[i], "-l") && (argc - i > 1)) {
            rilLibPath = argv[i + 1];
            i += 2;
	} else if (0 == strcmp(argv[i], "-c") && (argc - i > 1)) {
	    strncpy(client, argv[i+1], strlen(client));
	    i += 2;
        } else if (0 == strcmp(argv[i], "--")) {
            i++;
            hasLibArgs = 1;
	    memcpy(&s_argv[j], &argv[i], argc-i);
            break;
        } else {
            usage(argv[0]);
        }
    }
    if (strcmp(client, "0") == 0) {
	RIL_setRilSocketName("rild");
    } else if (strcmp(client, "1") == 0) {
	RIL_setRilSocketName("rild1");
    }

    if (rilLibPath == NULL) {
        if ( 0 == property_get(LIB_PATH_PROPERTY, libPath, NULL)) {
            // No lib sepcified on the command line, and nothing set in props.
            // Assume "no-ril" case.
            goto done;
        } else {
            rilLibPath = libPath;
        }
    }

    /* special override when in the emulator */
#if 1
    {
        static char   arg_device[32];
        int           done = 0;

#define  REFERENCE_RIL_PATH  "/system/lib/libreference-ril.so"

        /* first, read /proc/cmdline into memory */
        char          buffer[1024], *p, *q;
        int           len;
        int           fd = open("/proc/cmdline",O_RDONLY);

        if (fd < 0) {
            ALOGD("could not open /proc/cmdline:%s", strerror(errno));
            goto OpenLib;
        }

        do {
            len = read(fd,buffer,sizeof(buffer)); }
        while (len == -1 && errno == EINTR);

        if (len < 0) {
            ALOGD("could not read /proc/cmdline:%s", strerror(errno));
            close(fd);
            goto OpenLib;
        }
        close(fd);

        if (strstr(buffer, "android.qemud=") != NULL)
        {
            /* the qemud daemon is launched after rild, so
            * give it some time to create its GSM socket
            */
            int  tries = 5;
#define  QEMUD_SOCKET_NAME    "qemud"

            while (1) {
                int  fd;

                sleep(1);

                fd = qemu_pipe_open("qemud:gsm");
                if (fd < 0) {
                    fd = socket_local_client(
                                QEMUD_SOCKET_NAME,
                                ANDROID_SOCKET_NAMESPACE_RESERVED,
                                SOCK_STREAM );
                }
                if (fd >= 0) {
                    close(fd);
                    snprintf( arg_device, sizeof(arg_device), "%s/%s",
                                ANDROID_SOCKET_DIR, QEMUD_SOCKET_NAME );

                    memset(s_argv, 0, sizeof(s_argv));
                    s_argv[1] = "-s";
		    s_argv[2] = arg_device;
                    done = 1;
                    break;
                }
                ALOGD("could not connect to %s socket: %s",
                    QEMUD_SOCKET_NAME, strerror(errno));
                if (--tries == 0)
                    break;
            }
            if (!done) {
                ALOGE("could not connect to %s socket (giving up): %s",
                    QEMUD_SOCKET_NAME, strerror(errno));
                while(1)
                    sleep(0x00ffffff);
            }
        }

        /* otherwise, try to see if we passed a device name from the kernel */
        if (!done) do {
#define  KERNEL_OPTION  "android.ril="
#define  DEV_PREFIX     "/dev/"

            p = strstr( buffer, KERNEL_OPTION );
            if (p == NULL)
                break;

            p += sizeof(KERNEL_OPTION)-1;
            q  = strpbrk( p, " \t\n\r" );
            if (q != NULL)
                *q = 0;

            snprintf( arg_device, sizeof(arg_device), DEV_PREFIX "%s", p );
            arg_device[sizeof(arg_device)-1] = 0;
            memset(s_argv, 0, sizeof(s_argv));
            s_argv[1] = "-d";
	    s_argv[2] = arg_device;
            done = 1;

        } while (0);

        if (done) {
            argc = 3;
            i    = 1;
            hasLibArgs = 1;
            rilLibPath = REFERENCE_RIL_PATH;
            ALOGD("overriding with %s %s", s_argv[1], s_argv[2]);
        }
    }
OpenLib:
#endif
    switchUser();

#if 1 //for mux
    {//if(1 == DSDARIL_modem_dev){
        pthread_t s_tid_openserial;
        pthread_attr_t attr1;
        pthread_attr_init (&attr1);
        pthread_attr_setdetachstate(&attr1, PTHREAD_CREATE_DETACHED);
        pthread_create(&s_tid_openserial, &attr1, openSerial, NULL);
    }    
#endif

    dlHandle = dlopen(rilLibPath, RTLD_NOW);

    if (dlHandle == NULL) {
	ALOGE("**dl open failed **");
        fprintf(stderr, "dlopen failed: %s\n", dlerror());
        exit(-1);
    }

    RIL_startEventLoop();

    rilInit = (const RIL_RadioFunctions *(*)(const struct RIL_Env *, int, char **))dlsym(dlHandle, "RIL_Init");

    if (rilInit == NULL) {
        fprintf(stderr, "RIL_Init not defined or exported in %s\n", rilLibPath);
        exit(-1);
    }

////////////////////////////////////////////////////////////////////////////////
    //add DSDARIL
    if (isMultiSimEnabled() && !isMultiRild()){
        ALOGE("dlopen DSDARILLibPath: %s",DSDARILPATH);

        simdlHandle = dlopen(DSDARILPATH, RTLD_NOW);

        if (simdlHandle == NULL) {
            ALOGE("**dl open DSDARIL failed **");
            fprintf(stderr, "dlopen failed: %s\n", dlerror());
            exit(-1);
        }
        DSDARILInit = (const RIL_RadioFunctions *(*)(const struct RIL_Env *, int, char **))dlsym(simdlHandle, "RIL_Init");

        if (DSDARILInit == NULL) {
            ALOGE("**get DSDARIL RIL_Init() failed **");
            fprintf(stderr, "RIL_Init not defined or exported in %s\n", DSDARILPATH);
            exit(-1);
        }
#if 0   //for SKU2, not for SKU1
        //add for switching sim0 between CDMA and GSM
        simdlHandle_for_sim0 = dlopen(DSDARILPATH0, RTLD_NOW);

        if (simdlHandle_for_sim0 == NULL) {
            ALOGE("**dl open DSDARIL for sim0 failed **");
            fprintf(stderr, "dlopen for sim0 failed: %s\n", dlerror());
            //exit(-1);
        }else{
            DSDARILInit_for_sim0 = (const RIL_RadioFunctions *(*)(const struct RIL_Env *, int, char **))dlsym(simdlHandle_for_sim0, "RIL_Init");

            if (DSDARILInit_for_sim0 == NULL) {
                ALOGE("**get DSDARIL RIL_Init() for sim0 failed **");
                fprintf(stderr, "RIL_Init not defined or exported for sim0 in %s\n", DSDARILPATH0);
                //exit(-1);
            }
        }
#endif
    }
////////////////////////////////////////////////////////////////////////////////

    if (hasLibArgs) {
        argc = argc-i+1;
    } else {
        static char * newArgv[MAX_LIB_ARGS];
        static char args[PROPERTY_VALUE_MAX];
        property_get(LIB_ARGS_PROPERTY, args, "");
        argc = make_argv(args, s_argv);
    }

    // Make sure there's a reasonable argv[0]
    s_argv[0] = argv[0];

    s_argv[argc++] = "-c";
    s_argv[argc++] = client;

    ALOGE("RIL_Init argc = %d client = %s",argc, s_argv[argc-1]);
    funcs_inst[0] = rilInit(&s_rilEnv, argc, s_argv);
    if (isMultiSimEnabled() && !isMultiRild()) {
	s_argv[argc-1] = "1";  //client id incase of single rild managing two instances of RIL
        ALOGE("RIL_Init argc = %d client = %s",argc, s_argv[argc-1]);
        funcs_inst[1] = DSDARILInit(&s_rilEnv2, argc, s_argv);
        numClients++;

#if 0   // for SKU2, not for SKU1
        if(NULL == DSDARILInit_for_sim0){
        }else{
            //add for switching sim0 between CDMA and GSM
            s_argv[argc-1] = "0";  //client id incase of single rild managing two instances of RIL for sim0
            ALOGE("RIL_Init for sim 0 argc = %d client = %s",argc, s_argv[argc-1]);
            funcs_inst_for_sim0[0] = DSDARILInit_for_sim0(&s_rilEnv, argc, s_argv);
            if(NULL == funcs_inst_for_sim0[0]){
                ALOGE("RIL_Init for sim 0 fail ");
            }
        }
#endif
    }

    RIL_setMaxNumClients(numClients);

    ALOGD("Register the callbacks func received from RIL Init");
    for (i = 0; i < numClients; i++) {
        RIL_register(funcs_inst[i], i);
    }

#if 0 //for SKU2, not for SKU1
    if(NULL == DSDARILInit_for_sim0){
    }else{
        //add for switching sim0 between CDMA and GSM
        res = pthread_create(&a_thread, NULL, thread_function, NULL);
        if(0 != res){
            ALOGE("RILD pthread_create fail, res = %d ",res);
        }
    }
#endif

done:

    while(1) {
        // sleep(UINT32_MAX) seems to return immediately on bionic
        sleep(0x00ffffff);
    }
}

#if 0  //for SKU9-TEMP
int isMultiSimEnabled()
{
    int enabled = 0;
    char prop_val[PROPERTY_VALUE_MAX];
    if (property_get("persist.dsds.enabled", prop_val, "0") > 0)
    {
        if (strncmp(prop_val, "true", 4) == 0) {
            enabled = 1;
        }
        ALOGE("isMultiSimEnabled: prop_val = %s enabled = %d", prop_val, enabled);
    }
    return enabled;
}
#else
static int isMultiSimEnabled()
{
    int enabled = 0;
    char prop_val[PROPERTY_VALUE_MAX];
    if (property_get("persist.multisim.config", prop_val, "0") > 0)
    {
        if ((strncmp(prop_val, "dsds", 4) == 0) || (strncmp(prop_val, "dsda", 4) == 0)) {
            enabled = 1;
        }
        ALOGE("isMultiSimEnabled: prop_val = %s enabled = %d", prop_val, enabled);
    }
    return enabled;
}
#endif

static int isMultiRild()
{
    int enabled = 0;
    char prop_val[PROPERTY_VALUE_MAX];
    if (property_get("ro.multi.rild", prop_val, "0") > 0)
    {
        if (strncmp(prop_val, "true", 4) == 0) {
            enabled = 1;
        }
       ALOGD("isMultiRild: prop_val = %s enabled = %d", prop_val, enabled);
    }
    return enabled;
}

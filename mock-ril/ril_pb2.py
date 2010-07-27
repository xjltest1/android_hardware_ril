# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='ril.proto',
  package='ril_proto',
  serialized_pb='\n\tril.proto\x12\tril_proto\"\x9a\x02\n\x0cRilAppStatus\x12\'\n\x08\x61pp_type\x18\x01 \x01(\x0e\x32\x15.ril_proto.RilAppType\x12)\n\tapp_state\x18\x02 \x01(\x0e\x32\x16.ril_proto.RilAppState\x12\x33\n\x0eperso_substate\x18\x03 \x01(\x0e\x32\x1b.ril_proto.RilPersoSubstate\x12\x0b\n\x03\x61id\x18\x04 \x01(\t\x12\x11\n\tapp_label\x18\x05 \x01(\t\x12\x15\n\rpin1_replaced\x18\x06 \x01(\x05\x12$\n\x04pin1\x18\x07 \x01(\x0e\x32\x16.ril_proto.RilPinState\x12$\n\x04pin2\x18\x08 \x01(\x0e\x32\x16.ril_proto.RilPinState\"\x88\x02\n\rRilCardStatus\x12+\n\ncard_state\x18\x01 \x01(\x0e\x32\x17.ril_proto.RilCardState\x12\x33\n\x13universal_pin_state\x18\x02 \x01(\x0e\x32\x16.ril_proto.RilPinState\x12\'\n\x1fgsm_umts_subscription_app_index\x18\x03 \x01(\x05\x12#\n\x1b\x63\x64ma_subscription_app_index\x18\x04 \x01(\x05\x12\x18\n\x10num_applications\x18\x05 \x01(\x05\x12-\n\x0c\x61pplications\x18\x06 \x03(\x0b\x32\x17.ril_proto.RilAppStatus\"\x11\n\x0fReqGetSimStatus\"@\n\x0fRspGetSimStatus\x12-\n\x0b\x63\x61rd_status\x18\x01 \x02(\x0b\x32\x18.ril_proto.RilCardStatus\"\x1d\n\x0eReqEnterSimPin\x12\x0b\n\x03pin\x18\x01 \x02(\t\"+\n\x0eRspEnterSimPin\x12\x19\n\x11retries_remaining\x18\x01 \x02(\x05\"%\n\tReqHangUp\x12\x18\n\x10\x63onnection_index\x18\x01 \x02(\x05\"\x1f\n\x0eReqScreenState\x12\r\n\x05state\x18\x01 \x02(\x08*a\n\nRilCommand\x12\x16\n\x12\x43MD_GET_SIM_STATUS\x10\x01\x12\x15\n\x11\x43MD_ENTER_SIM_PIN\x10\x02\x12\x0e\n\nCMD_HANGUP\x10\x0c\x12\x14\n\x10\x43MD_SCREEN_STATE\x10=*\xb9\x02\n\nRadioState\x12\x13\n\x0fRADIO_STATE_OFF\x10\x00\x12\x1b\n\x17RADIO_STATE_UNAVAILABLE\x10\x01\x12\x1d\n\x19RADIO_STATE_SIM_NOT_READY\x10\x02\x12$\n RADIO_STATE_SIM_LOCKED_OR_ABSENT\x10\x03\x12\x19\n\x15RADIO_STATE_SIM_READY\x10\x04\x12\x1e\n\x1aRADIO_STATE_RUIM_NOT_READY\x10\x05\x12\x1a\n\x16RADIO_STATE_RUIM_READY\x10\x06\x12%\n!RADIO_STATE_RUIM_LOCKED_OR_ABSENT\x10\x07\x12\x1c\n\x18RADIO_STATE_NV_NOT_READY\x10\x08\x12\x18\n\x14RADIO_STATE_NV_READY\x10\t*P\n\x0cRilCardState\x12\x14\n\x10\x43\x41RDSTATE_ABSENT\x10\x00\x12\x15\n\x11\x43\x41RDSTATE_PRESENT\x10\x01\x12\x13\n\x0f\x43\x41RDSTATE_ERROR\x10\x02*\xf1\x06\n\x10RilPersoSubstate\x12\x19\n\x15PERSOSUBSTATE_UNKNOWN\x10\x00\x12\x1d\n\x19PERSOSUBSTATE_IN_PROGRESS\x10\x01\x12\x17\n\x13PERSOSUBSTATE_READY\x10\x02\x12\x1d\n\x19PERSOSUBSTATE_SIM_NETWORK\x10\x03\x12$\n PERSOSUBSTATE_SIM_NETWORK_SUBSET\x10\x04\x12\x1f\n\x1bPERSOSUBSTATE_SIM_CORPORATE\x10\x05\x12&\n\"PERSOSUBSTATE_SIM_SERVICE_PROVIDER\x10\x06\x12\x19\n\x15PERSOSUBSTATE_SIM_SIM\x10\x07\x12!\n\x1dPERSOSUBSTATE_SIM_NETWORK_PUK\x10\x08\x12(\n$PERSOSUBSTATE_SIM_NETWORK_SUBSET_PUK\x10\t\x12#\n\x1fPERSOSUBSTATE_SIM_CORPORATE_PUK\x10\n\x12*\n&PERSOSUBSTATE_SIM_SERVICE_PROVIDER_PUK\x10\x0b\x12\x1d\n\x19PERSOSUBSTATE_SIM_SIM_PUK\x10\x0c\x12\x1f\n\x1bPERSOSUBSTATE_RUIM_NETWORK1\x10\r\x12\x1f\n\x1bPERSOSUBSTATE_RUIM_NETWORK2\x10\x0e\x12\x1b\n\x17PERSOSUBSTATE_RUIM_HRPD\x10\x0f\x12 \n\x1cPERSOSUBSTATE_RUIM_CORPORATE\x10\x10\x12\'\n#PERSOSUBSTATE_RUIM_SERVICE_PROVIDER\x10\x11\x12\x1b\n\x17PERSOSUBSTATE_RUIM_RUIM\x10\x12\x12#\n\x1fPERSOSUBSTATE_RUIM_NETWORK1_PUK\x10\x13\x12#\n\x1fPERSOSUBSTATE_RUIM_NETWORK2_PUK\x10\x14\x12\x1f\n\x1bPERSOSUBSTATE_RUIM_HRPD_PUK\x10\x15\x12$\n PERSOSUBSTATE_RUIM_CORPORATE_PUK\x10\x16\x12+\n\'PERSOSUBSTATE_RUIM_SERVICE_PROVIDER_PUK\x10\x17\x12\x1f\n\x1bPERSOSUBSTATE_RUIM_RUIM_PUK\x10\x18*\x93\x01\n\x0bRilAppState\x12\x14\n\x10\x41PPSTATE_UNKNOWN\x10\x00\x12\x15\n\x11\x41PPSTATE_DETECTED\x10\x01\x12\x10\n\x0c\x41PPSTATE_PIN\x10\x02\x12\x10\n\x0c\x41PPSTATE_PUK\x10\x03\x12\x1f\n\x1b\x41PPSTATE_SUBSCRIPTION_PERSO\x10\x04\x12\x12\n\x0e\x41PPSTATE_READY\x10\x05*\xbd\x01\n\x0bRilPinState\x12\x14\n\x10PINSTATE_UNKNOWN\x10\x00\x12!\n\x1dPINSTATE_ENABLED_NOT_VERIFIED\x10\x01\x12\x1d\n\x19PINSTATE_ENABLED_VERIFIED\x10\x02\x12\x15\n\x11PINSTATE_DISABLED\x10\x03\x12\x1c\n\x18PINSTATE_ENABLED_BLOCKED\x10\x04\x12!\n\x1dPINSTATE_ENABLED_PERM_BLOCKED\x10\x05*h\n\nRilAppType\x12\x13\n\x0f\x41PPTYPE_UNKNOWN\x10\x00\x12\x0f\n\x0b\x41PPTYPE_SIM\x10\x01\x12\x10\n\x0c\x41PPTYPE_USIM\x10\x02\x12\x10\n\x0c\x41PPTYPE_RUIM\x10\x03\x12\x10\n\x0c\x41PPTYPE_CSIM\x10\x04\x42\x33\n(com.android.internal.telephony.ril_protoB\x07RilCmds')

_RILCOMMAND = descriptor.EnumDescriptor(
  name='RilCommand',
  full_name='ril_proto.RilCommand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CMD_GET_SIM_STATUS', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CMD_ENTER_SIM_PIN', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CMD_HANGUP', index=2, number=12,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CMD_SCREEN_STATE', index=3, number=61,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=809,
  serialized_end=906,
)


_RADIOSTATE = descriptor.EnumDescriptor(
  name='RadioState',
  full_name='ril_proto.RadioState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_OFF', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_UNAVAILABLE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_SIM_NOT_READY', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_SIM_LOCKED_OR_ABSENT', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_SIM_READY', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_RUIM_NOT_READY', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_RUIM_READY', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_RUIM_LOCKED_OR_ABSENT', index=7, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_NV_NOT_READY', index=8, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIO_STATE_NV_READY', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=909,
  serialized_end=1222,
)


_RILCARDSTATE = descriptor.EnumDescriptor(
  name='RilCardState',
  full_name='ril_proto.RilCardState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CARDSTATE_ABSENT', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CARDSTATE_PRESENT', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CARDSTATE_ERROR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1224,
  serialized_end=1304,
)


_RILPERSOSUBSTATE = descriptor.EnumDescriptor(
  name='RilPersoSubstate',
  full_name='ril_proto.RilPersoSubstate',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_IN_PROGRESS', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_READY', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_NETWORK', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_NETWORK_SUBSET', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_CORPORATE', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_SERVICE_PROVIDER', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_SIM', index=7, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_NETWORK_PUK', index=8, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_NETWORK_SUBSET_PUK', index=9, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_CORPORATE_PUK', index=10, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_SERVICE_PROVIDER_PUK', index=11, number=11,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_SIM_SIM_PUK', index=12, number=12,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_NETWORK1', index=13, number=13,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_NETWORK2', index=14, number=14,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_HRPD', index=15, number=15,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_CORPORATE', index=16, number=16,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_SERVICE_PROVIDER', index=17, number=17,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_RUIM', index=18, number=18,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_NETWORK1_PUK', index=19, number=19,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_NETWORK2_PUK', index=20, number=20,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_HRPD_PUK', index=21, number=21,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_CORPORATE_PUK', index=22, number=22,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_SERVICE_PROVIDER_PUK', index=23, number=23,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PERSOSUBSTATE_RUIM_RUIM_PUK', index=24, number=24,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1307,
  serialized_end=2188,
)


_RILAPPSTATE = descriptor.EnumDescriptor(
  name='RilAppState',
  full_name='ril_proto.RilAppState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='APPSTATE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPSTATE_DETECTED', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPSTATE_PIN', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPSTATE_PUK', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPSTATE_SUBSCRIPTION_PERSO', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPSTATE_READY', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2191,
  serialized_end=2338,
)


_RILPINSTATE = descriptor.EnumDescriptor(
  name='RilPinState',
  full_name='ril_proto.RilPinState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='PINSTATE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PINSTATE_ENABLED_NOT_VERIFIED', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PINSTATE_ENABLED_VERIFIED', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PINSTATE_DISABLED', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PINSTATE_ENABLED_BLOCKED', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PINSTATE_ENABLED_PERM_BLOCKED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2341,
  serialized_end=2530,
)


_RILAPPTYPE = descriptor.EnumDescriptor(
  name='RilAppType',
  full_name='ril_proto.RilAppType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='APPTYPE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPTYPE_SIM', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPTYPE_USIM', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPTYPE_RUIM', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='APPTYPE_CSIM', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2532,
  serialized_end=2636,
)


CMD_GET_SIM_STATUS = 1
CMD_ENTER_SIM_PIN = 2
CMD_HANGUP = 12
CMD_SCREEN_STATE = 61
RADIO_STATE_OFF = 0
RADIO_STATE_UNAVAILABLE = 1
RADIO_STATE_SIM_NOT_READY = 2
RADIO_STATE_SIM_LOCKED_OR_ABSENT = 3
RADIO_STATE_SIM_READY = 4
RADIO_STATE_RUIM_NOT_READY = 5
RADIO_STATE_RUIM_READY = 6
RADIO_STATE_RUIM_LOCKED_OR_ABSENT = 7
RADIO_STATE_NV_NOT_READY = 8
RADIO_STATE_NV_READY = 9
CARDSTATE_ABSENT = 0
CARDSTATE_PRESENT = 1
CARDSTATE_ERROR = 2
PERSOSUBSTATE_UNKNOWN = 0
PERSOSUBSTATE_IN_PROGRESS = 1
PERSOSUBSTATE_READY = 2
PERSOSUBSTATE_SIM_NETWORK = 3
PERSOSUBSTATE_SIM_NETWORK_SUBSET = 4
PERSOSUBSTATE_SIM_CORPORATE = 5
PERSOSUBSTATE_SIM_SERVICE_PROVIDER = 6
PERSOSUBSTATE_SIM_SIM = 7
PERSOSUBSTATE_SIM_NETWORK_PUK = 8
PERSOSUBSTATE_SIM_NETWORK_SUBSET_PUK = 9
PERSOSUBSTATE_SIM_CORPORATE_PUK = 10
PERSOSUBSTATE_SIM_SERVICE_PROVIDER_PUK = 11
PERSOSUBSTATE_SIM_SIM_PUK = 12
PERSOSUBSTATE_RUIM_NETWORK1 = 13
PERSOSUBSTATE_RUIM_NETWORK2 = 14
PERSOSUBSTATE_RUIM_HRPD = 15
PERSOSUBSTATE_RUIM_CORPORATE = 16
PERSOSUBSTATE_RUIM_SERVICE_PROVIDER = 17
PERSOSUBSTATE_RUIM_RUIM = 18
PERSOSUBSTATE_RUIM_NETWORK1_PUK = 19
PERSOSUBSTATE_RUIM_NETWORK2_PUK = 20
PERSOSUBSTATE_RUIM_HRPD_PUK = 21
PERSOSUBSTATE_RUIM_CORPORATE_PUK = 22
PERSOSUBSTATE_RUIM_SERVICE_PROVIDER_PUK = 23
PERSOSUBSTATE_RUIM_RUIM_PUK = 24
APPSTATE_UNKNOWN = 0
APPSTATE_DETECTED = 1
APPSTATE_PIN = 2
APPSTATE_PUK = 3
APPSTATE_SUBSCRIPTION_PERSO = 4
APPSTATE_READY = 5
PINSTATE_UNKNOWN = 0
PINSTATE_ENABLED_NOT_VERIFIED = 1
PINSTATE_ENABLED_VERIFIED = 2
PINSTATE_DISABLED = 3
PINSTATE_ENABLED_BLOCKED = 4
PINSTATE_ENABLED_PERM_BLOCKED = 5
APPTYPE_UNKNOWN = 0
APPTYPE_SIM = 1
APPTYPE_USIM = 2
APPTYPE_RUIM = 3
APPTYPE_CSIM = 4



_RILAPPSTATUS = descriptor.Descriptor(
  name='RilAppStatus',
  full_name='ril_proto.RilAppStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='app_type', full_name='ril_proto.RilAppStatus.app_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='app_state', full_name='ril_proto.RilAppStatus.app_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='perso_substate', full_name='ril_proto.RilAppStatus.perso_substate', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='aid', full_name='ril_proto.RilAppStatus.aid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='app_label', full_name='ril_proto.RilAppStatus.app_label', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin1_replaced', full_name='ril_proto.RilAppStatus.pin1_replaced', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin1', full_name='ril_proto.RilAppStatus.pin1', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin2', full_name='ril_proto.RilAppStatus.pin2', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=25,
  serialized_end=307,
)


_RILCARDSTATUS = descriptor.Descriptor(
  name='RilCardStatus',
  full_name='ril_proto.RilCardStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='card_state', full_name='ril_proto.RilCardStatus.card_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='universal_pin_state', full_name='ril_proto.RilCardStatus.universal_pin_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gsm_umts_subscription_app_index', full_name='ril_proto.RilCardStatus.gsm_umts_subscription_app_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cdma_subscription_app_index', full_name='ril_proto.RilCardStatus.cdma_subscription_app_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='num_applications', full_name='ril_proto.RilCardStatus.num_applications', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='applications', full_name='ril_proto.RilCardStatus.applications', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=310,
  serialized_end=574,
)


_REQGETSIMSTATUS = descriptor.Descriptor(
  name='ReqGetSimStatus',
  full_name='ril_proto.ReqGetSimStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=576,
  serialized_end=593,
)


_RSPGETSIMSTATUS = descriptor.Descriptor(
  name='RspGetSimStatus',
  full_name='ril_proto.RspGetSimStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='card_status', full_name='ril_proto.RspGetSimStatus.card_status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=595,
  serialized_end=659,
)


_REQENTERSIMPIN = descriptor.Descriptor(
  name='ReqEnterSimPin',
  full_name='ril_proto.ReqEnterSimPin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pin', full_name='ril_proto.ReqEnterSimPin.pin', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=661,
  serialized_end=690,
)


_RSPENTERSIMPIN = descriptor.Descriptor(
  name='RspEnterSimPin',
  full_name='ril_proto.RspEnterSimPin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='retries_remaining', full_name='ril_proto.RspEnterSimPin.retries_remaining', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=692,
  serialized_end=735,
)


_REQHANGUP = descriptor.Descriptor(
  name='ReqHangUp',
  full_name='ril_proto.ReqHangUp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='connection_index', full_name='ril_proto.ReqHangUp.connection_index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=737,
  serialized_end=774,
)


_REQSCREENSTATE = descriptor.Descriptor(
  name='ReqScreenState',
  full_name='ril_proto.ReqScreenState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='state', full_name='ril_proto.ReqScreenState.state', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=776,
  serialized_end=807,
)


_RILAPPSTATUS.fields_by_name['app_type'].enum_type = _RILAPPTYPE
_RILAPPSTATUS.fields_by_name['app_state'].enum_type = _RILAPPSTATE
_RILAPPSTATUS.fields_by_name['perso_substate'].enum_type = _RILPERSOSUBSTATE
_RILAPPSTATUS.fields_by_name['pin1'].enum_type = _RILPINSTATE
_RILAPPSTATUS.fields_by_name['pin2'].enum_type = _RILPINSTATE
_RILCARDSTATUS.fields_by_name['card_state'].enum_type = _RILCARDSTATE
_RILCARDSTATUS.fields_by_name['universal_pin_state'].enum_type = _RILPINSTATE
_RILCARDSTATUS.fields_by_name['applications'].message_type = _RILAPPSTATUS
_RSPGETSIMSTATUS.fields_by_name['card_status'].message_type = _RILCARDSTATUS

class RilAppStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RILAPPSTATUS
  
  # @@protoc_insertion_point(class_scope:ril_proto.RilAppStatus)

class RilCardStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RILCARDSTATUS
  
  # @@protoc_insertion_point(class_scope:ril_proto.RilCardStatus)

class ReqGetSimStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQGETSIMSTATUS
  
  # @@protoc_insertion_point(class_scope:ril_proto.ReqGetSimStatus)

class RspGetSimStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPGETSIMSTATUS
  
  # @@protoc_insertion_point(class_scope:ril_proto.RspGetSimStatus)

class ReqEnterSimPin(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQENTERSIMPIN
  
  # @@protoc_insertion_point(class_scope:ril_proto.ReqEnterSimPin)

class RspEnterSimPin(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPENTERSIMPIN
  
  # @@protoc_insertion_point(class_scope:ril_proto.RspEnterSimPin)

class ReqHangUp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQHANGUP
  
  # @@protoc_insertion_point(class_scope:ril_proto.ReqHangUp)

class ReqScreenState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQSCREENSTATE
  
  # @@protoc_insertion_point(class_scope:ril_proto.ReqScreenState)

# @@protoc_insertion_point(module_scope)
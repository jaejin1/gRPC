# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hi.proto',
  package='higrpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x08hi.proto\x12\x06higrpc\"\x19\n\tHiRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1a\n\x07HiReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\x96\x01\n\x02Hi\x12-\n\x05SayHi\x12\x11.higrpc.HiRequest\x1a\x0f.higrpc.HiReply\"\x00\x12/\n\x07\x43ountHi\x12\x11.higrpc.HiRequest\x1a\x0f.higrpc.HiReply\"\x00\x12\x30\n\x08JaejinHi\x12\x11.higrpc.HiRequest\x1a\x0f.higrpc.HiReply\"\x00\x62\x06proto3')
)




_HIREQUEST = _descriptor.Descriptor(
  name='HiRequest',
  full_name='higrpc.HiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='higrpc.HiRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=45,
)


_HIREPLY = _descriptor.Descriptor(
  name='HiReply',
  full_name='higrpc.HiReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='higrpc.HiReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['HiRequest'] = _HIREQUEST
DESCRIPTOR.message_types_by_name['HiReply'] = _HIREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HiRequest = _reflection.GeneratedProtocolMessageType('HiRequest', (_message.Message,), {
  'DESCRIPTOR' : _HIREQUEST,
  '__module__' : 'hi_pb2'
  # @@protoc_insertion_point(class_scope:higrpc.HiRequest)
  })
_sym_db.RegisterMessage(HiRequest)

HiReply = _reflection.GeneratedProtocolMessageType('HiReply', (_message.Message,), {
  'DESCRIPTOR' : _HIREPLY,
  '__module__' : 'hi_pb2'
  # @@protoc_insertion_point(class_scope:higrpc.HiReply)
  })
_sym_db.RegisterMessage(HiReply)



_HI = _descriptor.ServiceDescriptor(
  name='Hi',
  full_name='higrpc.Hi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=76,
  serialized_end=226,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHi',
    full_name='higrpc.Hi.SayHi',
    index=0,
    containing_service=None,
    input_type=_HIREQUEST,
    output_type=_HIREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CountHi',
    full_name='higrpc.Hi.CountHi',
    index=1,
    containing_service=None,
    input_type=_HIREQUEST,
    output_type=_HIREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='JaejinHi',
    full_name='higrpc.Hi.JaejinHi',
    index=2,
    containing_service=None,
    input_type=_HIREQUEST,
    output_type=_HIREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HI)

DESCRIPTOR.services_by_name['Hi'] = _HI

# @@protoc_insertion_point(module_scope)

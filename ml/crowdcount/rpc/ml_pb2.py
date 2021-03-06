# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ml.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ml.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x08ml.proto\"\x1d\n\x0c\x43ountRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\"[\n\nCountReply\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65nsity_map\x18\x02 \x01(\x0c\x12\x13\n\x0b\x63rowd_count\x18\x03 \x01(\x02\x12\x12\n\nline_count\x18\x04 \x01(\x02\x32\\\n\x03RPC\x12*\n\nCountCrowd\x12\r.CountRequest\x1a\x0b.CountReply\"\x00\x12)\n\tCountLine\x12\r.CountRequest\x1a\x0b.CountReply\"\x00\x62\x06proto3')
)




_COUNTREQUEST = _descriptor.Descriptor(
  name='CountRequest',
  full_name='CountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='CountRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=41,
)


_COUNTREPLY = _descriptor.Descriptor(
  name='CountReply',
  full_name='CountReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='CountReply.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='density_map', full_name='CountReply.density_map', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crowd_count', full_name='CountReply.crowd_count', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_count', full_name='CountReply.line_count', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['CountRequest'] = _COUNTREQUEST
DESCRIPTOR.message_types_by_name['CountReply'] = _COUNTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CountRequest = _reflection.GeneratedProtocolMessageType('CountRequest', (_message.Message,), dict(
  DESCRIPTOR = _COUNTREQUEST,
  __module__ = 'ml_pb2'
  # @@protoc_insertion_point(class_scope:CountRequest)
  ))
_sym_db.RegisterMessage(CountRequest)

CountReply = _reflection.GeneratedProtocolMessageType('CountReply', (_message.Message,), dict(
  DESCRIPTOR = _COUNTREPLY,
  __module__ = 'ml_pb2'
  # @@protoc_insertion_point(class_scope:CountReply)
  ))
_sym_db.RegisterMessage(CountReply)



_RPC = _descriptor.ServiceDescriptor(
  name='RPC',
  full_name='RPC',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=136,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='CountCrowd',
    full_name='RPC.CountCrowd',
    index=0,
    containing_service=None,
    input_type=_COUNTREQUEST,
    output_type=_COUNTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CountLine',
    full_name='RPC.CountLine',
    index=1,
    containing_service=None,
    input_type=_COUNTREQUEST,
    output_type=_COUNTREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPC)

DESCRIPTOR.services_by_name['RPC'] = _RPC

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class RPCStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.CountCrowd = channel.unary_unary(
          '/RPC/CountCrowd',
          request_serializer=CountRequest.SerializeToString,
          response_deserializer=CountReply.FromString,
          )
      self.CountLine = channel.unary_unary(
          '/RPC/CountLine',
          request_serializer=CountRequest.SerializeToString,
          response_deserializer=CountReply.FromString,
          )


  class RPCServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def CountCrowd(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def CountLine(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_RPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CountCrowd': grpc.unary_unary_rpc_method_handler(
            servicer.CountCrowd,
            request_deserializer=CountRequest.FromString,
            response_serializer=CountReply.SerializeToString,
        ),
        'CountLine': grpc.unary_unary_rpc_method_handler(
            servicer.CountLine,
            request_deserializer=CountRequest.FromString,
            response_serializer=CountReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'RPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaRPCServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def CountCrowd(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def CountLine(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaRPCStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def CountCrowd(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    CountCrowd.future = None
    def CountLine(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    CountLine.future = None


  def beta_create_RPC_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('RPC', 'CountCrowd'): CountRequest.FromString,
      ('RPC', 'CountLine'): CountRequest.FromString,
    }
    response_serializers = {
      ('RPC', 'CountCrowd'): CountReply.SerializeToString,
      ('RPC', 'CountLine'): CountReply.SerializeToString,
    }
    method_implementations = {
      ('RPC', 'CountCrowd'): face_utilities.unary_unary_inline(servicer.CountCrowd),
      ('RPC', 'CountLine'): face_utilities.unary_unary_inline(servicer.CountLine),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_RPC_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('RPC', 'CountCrowd'): CountRequest.SerializeToString,
      ('RPC', 'CountLine'): CountRequest.SerializeToString,
    }
    response_deserializers = {
      ('RPC', 'CountCrowd'): CountReply.FromString,
      ('RPC', 'CountLine'): CountReply.FromString,
    }
    cardinalities = {
      'CountCrowd': cardinality.Cardinality.UNARY_UNARY,
      'CountLine': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'RPC', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: notification.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'notification.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12notification.proto\x12\x0cnotification\"W\n\x0ePaymentRequest\x12\x0e\n\x06\x63lient\x18\x01 \x01(\t\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x16\n\x0epayment_status\x18\x03 \x01(\t\x12\x0c\n\x04\x63ost\x18\x04 \x01(\x02\"\"\n\x0fPaymentResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2h\n\x13NotificationService\x12Q\n\x12NotificarPagamento\x12\x1c.notification.PaymentRequest\x1a\x1d.notification.PaymentResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PAYMENTREQUEST']._serialized_start=36
  _globals['_PAYMENTREQUEST']._serialized_end=123
  _globals['_PAYMENTRESPONSE']._serialized_start=125
  _globals['_PAYMENTRESPONSE']._serialized_end=159
  _globals['_NOTIFICATIONSERVICE']._serialized_start=161
  _globals['_NOTIFICATIONSERVICE']._serialized_end=265
# @@protoc_insertion_point(module_scope)

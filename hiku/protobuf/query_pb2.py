# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hiku/protobuf/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hiku/protobuf/query.proto',
  package='hiku.protobuf.query',
  syntax='proto3',
  serialized_pb=_b('\n\x19hiku/protobuf/query.proto\x12\x13hiku.protobuf.query\x1a\x1cgoogle/protobuf/struct.proto\"?\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"g\n\x04Link\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x07options\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x04node\x18\x02 \x01(\x0b\x32\x19.hiku.protobuf.query.Node\"g\n\x04Item\x12+\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x1a.hiku.protobuf.query.FieldH\x00\x12)\n\x04link\x18\x02 \x01(\x0b\x32\x19.hiku.protobuf.query.LinkH\x00\x42\x07\n\x05value\"0\n\x04Node\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.hiku.protobuf.query.Itemb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='hiku.protobuf.query.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hiku.protobuf.query.Field.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='hiku.protobuf.query.Field.options', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=143,
)


_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='hiku.protobuf.query.Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hiku.protobuf.query.Link.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='hiku.protobuf.query.Link.options', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node', full_name='hiku.protobuf.query.Link.node', index=2,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=248,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='hiku.protobuf.query.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='hiku.protobuf.query.Item.field', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link', full_name='hiku.protobuf.query.Item.link', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='hiku.protobuf.query.Item.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=250,
  serialized_end=353,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='hiku.protobuf.query.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='hiku.protobuf.query.Node.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=403,
)

_FIELD.fields_by_name['options'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LINK.fields_by_name['options'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LINK.fields_by_name['node'].message_type = _NODE
_ITEM.fields_by_name['field'].message_type = _FIELD
_ITEM.fields_by_name['link'].message_type = _LINK
_ITEM.oneofs_by_name['value'].fields.append(
  _ITEM.fields_by_name['field'])
_ITEM.fields_by_name['field'].containing_oneof = _ITEM.oneofs_by_name['value']
_ITEM.oneofs_by_name['value'].fields.append(
  _ITEM.fields_by_name['link'])
_ITEM.fields_by_name['link'].containing_oneof = _ITEM.oneofs_by_name['value']
_NODE.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.message_types_by_name['Link'] = _LINK
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['Node'] = _NODE

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), dict(
  DESCRIPTOR = _FIELD,
  __module__ = 'hiku.protobuf.query_pb2'
  # @@protoc_insertion_point(class_scope:hiku.protobuf.query.Field)
  ))
_sym_db.RegisterMessage(Field)

Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), dict(
  DESCRIPTOR = _LINK,
  __module__ = 'hiku.protobuf.query_pb2'
  # @@protoc_insertion_point(class_scope:hiku.protobuf.query.Link)
  ))
_sym_db.RegisterMessage(Link)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'hiku.protobuf.query_pb2'
  # @@protoc_insertion_point(class_scope:hiku.protobuf.query.Item)
  ))
_sym_db.RegisterMessage(Item)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'hiku.protobuf.query_pb2'
  # @@protoc_insertion_point(class_scope:hiku.protobuf.query.Node)
  ))
_sym_db.RegisterMessage(Node)


# @@protoc_insertion_point(module_scope)

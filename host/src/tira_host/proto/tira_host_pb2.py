# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tira_host.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tira_host.proto',
  package='tira.generated',
  syntax='proto3',
  serialized_options=b'\n\"de.webis.tira.client.web.generatedB\020TiraHostMessagesH\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0ftira_host.proto\x12\x0etira.generated\x1a\x1bgoogle/protobuf/empty.proto\"!\n\x11RequestVmCommands\x12\x0c\n\x04vmId\x18\x01 \x01(\t\"I\n\x0fRequestVmCreate\x12\x0f\n\x07ovaFile\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\t\x12\x15\n\rbulkCommandId\x18\x03 \x01(\t\"\xc8\x01\n\x15RequestRunExecuteEval\x12\x16\n\x0esubmissionFile\x18\x01 \x01(\t\x12\x16\n\x0einputDatasetId\x18\x02 \x01(\t\x12\x14\n\x0cinputRunPath\x18\x03 \x01(\t\x12\x15\n\routputDirName\x18\x04 \x01(\t\x12\x11\n\tsandboxed\x18\x05 \x01(\t\x12\r\n\x05runId\x18\x06 \x01(\t\x12\x14\n\x0csnapshotName\x18\x07 \x01(\t\x12\x1a\n\x12optionalParameters\x18\x08 \x01(\t\"L\n\x0bTransaction\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.tira.generated.Status\x12\x15\n\rtransactionId\x18\x02 \x01(\t\"j\n\nSetVmState\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.tira.generated.Status\x12&\n\x05state\x18\x02 \x01(\x0e\x32\x17.tira.generated.VmState\x12\x0c\n\x04vmId\x18\x03 \x01(\t\"\xf1\x01\n\x06VmInfo\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.tira.generated.Status\x12\x0f\n\x07guestOs\x18\x02 \x01(\t\x12\x12\n\nmemorySize\x18\x03 \x01(\t\x12\x14\n\x0cnumberOfCpus\x18\x04 \x01(\t\x12\x0f\n\x07sshPort\x18\x05 \x01(\t\x12\x0f\n\x07rdpPort\x18\x06 \x01(\t\x12\x0c\n\x04host\x18\x07 \x01(\t\x12\x15\n\rsshPortStatus\x18\x08 \x01(\x08\x12\x15\n\rrdpPortStatus\x18\t \x01(\x08\x12&\n\x05state\x18\n \x01(\x0e\x32\x17.tira.generated.VmState\"\xd4\x02\n\x0c\x43ommandState\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x36\n\x08\x63ommands\x18\x02 \x03(\x0b\x32$.tira.generated.CommandState.Command\x1a\xf9\x01\n\x07\x43ommand\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rcommandString\x18\x02 \x01(\t\x12\x11\n\tstartTime\x18\x03 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\t\x12;\n\x06status\x18\x05 \x01(\x0e\x32+.tira.generated.CommandState.Command.Status\x12\x0f\n\x07logFile\x18\x06 \x01(\t\x12\x12\n\nreturnCode\x18\x07 \x01(\x05\x12\x15\n\rbulkCommandId\x18\x08 \x01(\t\".\n\x06Status\x12\x0b\n\x07RUNNING\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02*!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01*\x98\x01\n\x07VmState\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0f\n\x0bPOWERED_OFF\x10\x02\x12\x0f\n\x0bPOWERING_ON\x10\x03\x12\x10\n\x0cPOWERING_OFF\x10\x04\x12\x0e\n\nSANDBOXING\x10\x05\x12\x10\n\x0cUNSANDBOXING\x10\x06\x12\r\n\tEXECUTING\x10\x07\x12\x0c\n\x08\x41RCHIVED\x10\x08\x32\x97\t\n\x0fTiraHostService\x12M\n\tvm_backup\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12K\n\tvm_create\x12\x1f.tira.generated.RequestVmCreate\x1a\x1b.tira.generated.Transaction\"\x00\x12M\n\tvm_delete\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12\x46\n\x07vm_info\x12!.tira.generated.RequestVmCommands\x1a\x16.tira.generated.VmInfo\"\x00\x12@\n\x07vm_list\x12\x16.google.protobuf.Empty\x1a\x1b.tira.generated.Transaction\"\x00\x12N\n\nvm_metrics\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12N\n\nvm_sandbox\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12O\n\x0bvm_shutdown\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12O\n\x0bvm_snapshot\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12L\n\x08vm_start\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12K\n\x07vm_stop\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12P\n\x0cvm_unsandbox\x12!.tira.generated.RequestVmCommands\x1a\x1b.tira.generated.Transaction\"\x00\x12S\n\x0brun_execute\x12%.tira.generated.RequestRunExecuteEval\x1a\x1b.tira.generated.Transaction\"\x00\x12P\n\x08run_eval\x12%.tira.generated.RequestRunExecuteEval\x1a\x1b.tira.generated.Transaction\"\x00\x12\x39\n\x05\x61live\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x32\xb4\x01\n\x16TiraApplicationService\x12\x46\n\tset_state\x12\x1a.tira.generated.SetVmState\x1a\x1b.tira.generated.Transaction\"\x00\x12R\n\x14\x63omplete_transaction\x12\x1b.tira.generated.Transaction\x1a\x1b.tira.generated.Transaction\"\x00\x42\x38\n\"de.webis.tira.client.web.generatedB\x10TiraHostMessagesH\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='tira.generated.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1150,
  serialized_end=1183,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_VMSTATE = _descriptor.EnumDescriptor(
  name='VmState',
  full_name='tira.generated.VmState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POWERED_OFF', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POWERING_ON', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POWERING_OFF', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SANDBOXING', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNSANDBOXING', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARCHIVED', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1186,
  serialized_end=1338,
)
_sym_db.RegisterEnumDescriptor(_VMSTATE)

VmState = enum_type_wrapper.EnumTypeWrapper(_VMSTATE)
SUCCESS = 0
FAILED = 1
UNDEFINED = 0
RUNNING = 1
POWERED_OFF = 2
POWERING_ON = 3
POWERING_OFF = 4
SANDBOXING = 5
UNSANDBOXING = 6
EXECUTING = 7
ARCHIVED = 8


_COMMANDSTATE_COMMAND_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='tira.generated.CommandState.Command.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1102,
  serialized_end=1148,
)
_sym_db.RegisterEnumDescriptor(_COMMANDSTATE_COMMAND_STATUS)


_REQUESTVMCOMMANDS = _descriptor.Descriptor(
  name='RequestVmCommands',
  full_name='tira.generated.RequestVmCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vmId', full_name='tira.generated.RequestVmCommands.vmId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=97,
)


_REQUESTVMCREATE = _descriptor.Descriptor(
  name='RequestVmCreate',
  full_name='tira.generated.RequestVmCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ovaFile', full_name='tira.generated.RequestVmCreate.ovaFile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userId', full_name='tira.generated.RequestVmCreate.userId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bulkCommandId', full_name='tira.generated.RequestVmCreate.bulkCommandId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=99,
  serialized_end=172,
)


_REQUESTRUNEXECUTEEVAL = _descriptor.Descriptor(
  name='RequestRunExecuteEval',
  full_name='tira.generated.RequestRunExecuteEval',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='submissionFile', full_name='tira.generated.RequestRunExecuteEval.submissionFile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputDatasetId', full_name='tira.generated.RequestRunExecuteEval.inputDatasetId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputRunPath', full_name='tira.generated.RequestRunExecuteEval.inputRunPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputDirName', full_name='tira.generated.RequestRunExecuteEval.outputDirName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sandboxed', full_name='tira.generated.RequestRunExecuteEval.sandboxed', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='runId', full_name='tira.generated.RequestRunExecuteEval.runId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snapshotName', full_name='tira.generated.RequestRunExecuteEval.snapshotName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='optionalParameters', full_name='tira.generated.RequestRunExecuteEval.optionalParameters', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=175,
  serialized_end=375,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='tira.generated.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='tira.generated.Transaction.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionId', full_name='tira.generated.Transaction.transactionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=377,
  serialized_end=453,
)


_SETVMSTATE = _descriptor.Descriptor(
  name='SetVmState',
  full_name='tira.generated.SetVmState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='tira.generated.SetVmState.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='tira.generated.SetVmState.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vmId', full_name='tira.generated.SetVmState.vmId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=455,
  serialized_end=561,
)


_VMINFO = _descriptor.Descriptor(
  name='VmInfo',
  full_name='tira.generated.VmInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='tira.generated.VmInfo.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='guestOs', full_name='tira.generated.VmInfo.guestOs', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memorySize', full_name='tira.generated.VmInfo.memorySize', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numberOfCpus', full_name='tira.generated.VmInfo.numberOfCpus', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sshPort', full_name='tira.generated.VmInfo.sshPort', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rdpPort', full_name='tira.generated.VmInfo.rdpPort', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='tira.generated.VmInfo.host', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sshPortStatus', full_name='tira.generated.VmInfo.sshPortStatus', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rdpPortStatus', full_name='tira.generated.VmInfo.rdpPortStatus', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='tira.generated.VmInfo.state', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=564,
  serialized_end=805,
)


_COMMANDSTATE_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='tira.generated.CommandState.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tira.generated.CommandState.Command.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commandString', full_name='tira.generated.CommandState.Command.commandString', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='tira.generated.CommandState.Command.startTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='tira.generated.CommandState.Command.endTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='tira.generated.CommandState.Command.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logFile', full_name='tira.generated.CommandState.Command.logFile', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='returnCode', full_name='tira.generated.CommandState.Command.returnCode', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bulkCommandId', full_name='tira.generated.CommandState.Command.bulkCommandId', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDSTATE_COMMAND_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=899,
  serialized_end=1148,
)

_COMMANDSTATE = _descriptor.Descriptor(
  name='CommandState',
  full_name='tira.generated.CommandState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='tira.generated.CommandState.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='tira.generated.CommandState.commands', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMMANDSTATE_COMMAND, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=808,
  serialized_end=1148,
)

_TRANSACTION.fields_by_name['status'].enum_type = _STATUS
_SETVMSTATE.fields_by_name['status'].enum_type = _STATUS
_SETVMSTATE.fields_by_name['state'].enum_type = _VMSTATE
_VMINFO.fields_by_name['status'].enum_type = _STATUS
_VMINFO.fields_by_name['state'].enum_type = _VMSTATE
_COMMANDSTATE_COMMAND.fields_by_name['status'].enum_type = _COMMANDSTATE_COMMAND_STATUS
_COMMANDSTATE_COMMAND.containing_type = _COMMANDSTATE
_COMMANDSTATE_COMMAND_STATUS.containing_type = _COMMANDSTATE_COMMAND
_COMMANDSTATE.fields_by_name['commands'].message_type = _COMMANDSTATE_COMMAND
DESCRIPTOR.message_types_by_name['RequestVmCommands'] = _REQUESTVMCOMMANDS
DESCRIPTOR.message_types_by_name['RequestVmCreate'] = _REQUESTVMCREATE
DESCRIPTOR.message_types_by_name['RequestRunExecuteEval'] = _REQUESTRUNEXECUTEEVAL
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['SetVmState'] = _SETVMSTATE
DESCRIPTOR.message_types_by_name['VmInfo'] = _VMINFO
DESCRIPTOR.message_types_by_name['CommandState'] = _COMMANDSTATE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['VmState'] = _VMSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestVmCommands = _reflection.GeneratedProtocolMessageType('RequestVmCommands', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTVMCOMMANDS,
  '__module__' : 'tira_host_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.RequestVmCommands)
  })
_sym_db.RegisterMessage(RequestVmCommands)

RequestVmCreate = _reflection.GeneratedProtocolMessageType('RequestVmCreate', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTVMCREATE,
  '__module__' : 'tira_host_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.RequestVmCreate)
  })
_sym_db.RegisterMessage(RequestVmCreate)

RequestRunExecuteEval = _reflection.GeneratedProtocolMessageType('RequestRunExecuteEval', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTRUNEXECUTEEVAL,
  '__module__' : 'tira_host_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.RequestRunExecuteEval)
  })
_sym_db.RegisterMessage(RequestRunExecuteEval)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'tira_host_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

SetVmState = _reflection.GeneratedProtocolMessageType('SetVmState', (_message.Message,), {
  'DESCRIPTOR' : _SETVMSTATE,
  '__module__' : 'tira_host_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.SetVmState)
  })
_sym_db.RegisterMessage(SetVmState)

VmInfo = _reflection.GeneratedProtocolMessageType('VmInfo', (_message.Message,), {
  'DESCRIPTOR' : _VMINFO,
  '__module__' : 'tira_host_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.VmInfo)
  })
_sym_db.RegisterMessage(VmInfo)

CommandState = _reflection.GeneratedProtocolMessageType('CommandState', (_message.Message,), {

  'Command' : _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
    'DESCRIPTOR' : _COMMANDSTATE_COMMAND,
    '__module__' : 'tira_host_pb2'
    # @@protoc_insertion_point(class_scope:tira.generated.CommandState.Command)
    })
  ,
  'DESCRIPTOR' : _COMMANDSTATE,
  '__module__' : 'tira_host_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.CommandState)
  })
_sym_db.RegisterMessage(CommandState)
_sym_db.RegisterMessage(CommandState.Command)


DESCRIPTOR._options = None

_TIRAHOSTSERVICE = _descriptor.ServiceDescriptor(
  name='TiraHostService',
  full_name='tira.generated.TiraHostService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1341,
  serialized_end=2516,
  methods=[
  _descriptor.MethodDescriptor(
    name='vm_backup',
    full_name='tira.generated.TiraHostService.vm_backup',
    index=0,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_create',
    full_name='tira.generated.TiraHostService.vm_create',
    index=1,
    containing_service=None,
    input_type=_REQUESTVMCREATE,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_delete',
    full_name='tira.generated.TiraHostService.vm_delete',
    index=2,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_info',
    full_name='tira.generated.TiraHostService.vm_info',
    index=3,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_VMINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_list',
    full_name='tira.generated.TiraHostService.vm_list',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_metrics',
    full_name='tira.generated.TiraHostService.vm_metrics',
    index=5,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_sandbox',
    full_name='tira.generated.TiraHostService.vm_sandbox',
    index=6,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_shutdown',
    full_name='tira.generated.TiraHostService.vm_shutdown',
    index=7,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_snapshot',
    full_name='tira.generated.TiraHostService.vm_snapshot',
    index=8,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_start',
    full_name='tira.generated.TiraHostService.vm_start',
    index=9,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_stop',
    full_name='tira.generated.TiraHostService.vm_stop',
    index=10,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_unsandbox',
    full_name='tira.generated.TiraHostService.vm_unsandbox',
    index=11,
    containing_service=None,
    input_type=_REQUESTVMCOMMANDS,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='run_execute',
    full_name='tira.generated.TiraHostService.run_execute',
    index=12,
    containing_service=None,
    input_type=_REQUESTRUNEXECUTEEVAL,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='run_eval',
    full_name='tira.generated.TiraHostService.run_eval',
    index=13,
    containing_service=None,
    input_type=_REQUESTRUNEXECUTEEVAL,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='alive',
    full_name='tira.generated.TiraHostService.alive',
    index=14,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIRAHOSTSERVICE)

DESCRIPTOR.services_by_name['TiraHostService'] = _TIRAHOSTSERVICE


_TIRAAPPLICATIONSERVICE = _descriptor.ServiceDescriptor(
  name='TiraApplicationService',
  full_name='tira.generated.TiraApplicationService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=2519,
  serialized_end=2699,
  methods=[
  _descriptor.MethodDescriptor(
    name='set_state',
    full_name='tira.generated.TiraApplicationService.set_state',
    index=0,
    containing_service=None,
    input_type=_SETVMSTATE,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='complete_transaction',
    full_name='tira.generated.TiraApplicationService.complete_transaction',
    index=1,
    containing_service=None,
    input_type=_TRANSACTION,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIRAAPPLICATIONSERVICE)

DESCRIPTOR.services_by_name['TiraApplicationService'] = _TIRAAPPLICATIONSERVICE

# @@protoc_insertion_point(module_scope)
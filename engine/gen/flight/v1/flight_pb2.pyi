import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProbeRequest(_message.Message):
    __slots__ = ("client_sent_at",)
    CLIENT_SENT_AT_FIELD_NUMBER: _ClassVar[int]
    client_sent_at: _timestamp_pb2.Timestamp
    def __init__(self, client_sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProbeResponse(_message.Message):
    __slots__ = ("client_sent_at", "server_processed_at", "cpu_percent", "memory_percent", "uptime_seconds")
    CLIENT_SENT_AT_FIELD_NUMBER: _ClassVar[int]
    SERVER_PROCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    client_sent_at: _timestamp_pb2.Timestamp
    server_processed_at: _timestamp_pb2.Timestamp
    cpu_percent: float
    memory_percent: float
    uptime_seconds: int
    def __init__(self, client_sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., server_processed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cpu_percent: _Optional[float] = ..., memory_percent: _Optional[float] = ..., uptime_seconds: _Optional[int] = ...) -> None: ...

import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlightEventRequest(_message.Message):
    __slots__ = ("message", "level")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    message: str
    level: str
    def __init__(self, message: _Optional[str] = ..., level: _Optional[str] = ...) -> None: ...

class FlightEventResponse(_message.Message):
    __slots__ = ("acknowledgment", "received_at")
    ACKNOWLEDGMENT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    acknowledgment: str
    received_at: _timestamp_pb2.Timestamp
    def __init__(self, acknowledgment: _Optional[str] = ..., received_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

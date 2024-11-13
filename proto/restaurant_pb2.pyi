from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor


class RestaurantRequest(_message.Message):
    __slots__ = ["items", "orderID"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[str]
    orderID: str
    def __init__(self, orderID: _Optional[str] = ...,
                 items: _Optional[_Iterable[str]] = ...) -> None: ...


class RestaurantResponse(_message.Message):
    __slots__ = ["itemMessage", "orderID", "status"]

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCEPTED: RestaurantResponse.Status
    ITEMMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    REJECTED: RestaurantResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    itemMessage: _containers.RepeatedCompositeFieldContainer[items]
    orderID: str
    status: RestaurantResponse.Status
    def __init__(self, orderID: _Optional[str] = ..., status: _Optional[_Union[RestaurantResponse.Status, str]]
                 = ..., itemMessage: _Optional[_Iterable[_Union[items, _Mapping]]] = ...) -> None: ...


class items(_message.Message):
    __slots__ = ["itemName"]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    itemName: str
    def __init__(self, itemName: _Optional[str] = ...) -> None: ...

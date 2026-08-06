from collections.abc import Callable
from typing import Generic, TypeVar, overload

T = TypeVar("T")
Owner = TypeVar("Owner")


class Validated(Generic[T]):
    def __init__(self, validator: Callable[[T], T]) -> None:
        self.validator = validator

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    @overload
    def __get__(self, instance: None, owner: type | None = None) -> "Validated[T]": ...

    @overload
    def __get__(self, instance: Owner, owner: type | None = None) -> T: ...

    def __get__(self, instance: Owner | None, owner: type | None = None):
        raise NotImplementedError

    def __set__(self, instance: object, value: T) -> None:
        raise NotImplementedError

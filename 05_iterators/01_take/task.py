from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def take(iterable: Iterable[T], count: int) -> list[T]:
    """Take at most count first values from an iterable."""
    # TODO: получите итератор через iter() и вызывайте next() не более count раз.
    raise NotImplementedError

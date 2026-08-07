from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def batched(iterable: Iterable[T], size: int) -> Iterator[tuple[T, ...]]:
    # TODO: реализуйте без преобразования iterable в список.
    raise NotImplementedError

from collections.abc import Iterable, Iterator
from queue import Queue
from typing import TypeVar

T = TypeVar("T")
DONE = object()


def fan_in(sources: Iterable[Queue[T | object]]) -> Iterator[T]:
    # TODO: по worker на источник и общая выходная очередь.
    raise NotImplementedError

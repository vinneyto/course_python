from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def merge_sorted(iterables: Iterable[Iterable[T]]) -> Iterator[T]:
    """Lazily merge already sorted iterables."""
    # TODO: не материализуйте входные последовательности.
    raise NotImplementedError

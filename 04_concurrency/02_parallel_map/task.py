from collections.abc import Callable, Iterable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")
R = TypeVar("R")


def parallel_map(fn: Callable[[T], R], items: Iterable[T], workers: int = 4) -> list[R]:
    # TODO: используйте concurrent.futures.ThreadPoolExecutor.
    raise NotImplementedError

from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def memoize(maxsize: int | None = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    # TODO: проверьте maxsize и реализуйте LRU-кеш в замыкании.
    raise NotImplementedError

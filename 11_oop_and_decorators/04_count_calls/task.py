from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def count_calls(func: Callable[P, R]) -> Callable[P, R]:
    # TODO: используйте замыкание, wraps и finally.
    raise NotImplementedError

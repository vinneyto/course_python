import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def retry(
    *,
    attempts: int = 3,
    exceptions: tuple[type[Exception], ...] = (Exception,),
    delay: float = 0,
    backoff: float = 1,
    sleep: Callable[[float], None] = time.sleep,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    # TODO: валидируйте параметры, используйте functools.wraps.
    raise NotImplementedError

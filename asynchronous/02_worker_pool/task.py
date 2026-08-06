from collections.abc import AsyncIterable, Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


async def async_map(
    fn: Callable[[T], Awaitable[R]], items: AsyncIterable[T], limit: int = 5
) -> list[R]:
    # TODO: ограниченная очередь + limit worker tasks.
    raise NotImplementedError

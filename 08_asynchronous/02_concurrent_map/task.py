from collections.abc import Awaitable, Callable, Iterable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


async def concurrent_map(
    func: Callable[[T], Awaitable[R]], values: Iterable[T]
) -> list[R]:
    """Run func for all values concurrently and preserve input order."""
    # TODO: создайте корутины для всех значений и передайте их в asyncio.gather().
    raise NotImplementedError

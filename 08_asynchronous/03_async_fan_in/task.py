from collections.abc import AsyncIterable, AsyncIterator, Iterable
from typing import TypeVar

T = TypeVar("T")


async def merge(sources: Iterable[AsyncIterable[T]]) -> AsyncIterator[T]:
    # TODO: создайте producer tasks и общую asyncio.Queue.
    raise NotImplementedError
    yield  # pragma: no cover

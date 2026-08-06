import asyncio

import pytest

from .task import merge


async def source(values, delay=0):
    for value in values:
        await asyncio.sleep(delay)
        yield value


@pytest.mark.asyncio
async def test_merges_sources_and_empty_input():
    assert sorted([item async for item in merge([source([1, 3]), source([2])])]) == [1, 2, 3]
    assert [item async for item in merge([])] == []


@pytest.mark.asyncio
async def test_propagates_producer_error():
    async def broken():
        yield 1
        raise LookupError("boom")

    with pytest.raises(LookupError, match="boom"):
        _ = [item async for item in merge([broken()])]

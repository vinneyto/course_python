import asyncio

import pytest

from .task import async_map


async def values(count):
    for i in range(count):
        yield i


@pytest.mark.asyncio
async def test_limits_concurrency_and_preserves_order():
    active = peak = 0
    lock = asyncio.Lock()

    async def work(value):
        nonlocal active, peak
        async with lock:
            active += 1
            peak = max(peak, active)
        await asyncio.sleep(0.001 * (5 - value))
        async with lock:
            active -= 1
        return value * 10

    assert await async_map(work, values(5), limit=2) == [0, 10, 20, 30, 40]
    assert peak == 2


@pytest.mark.asyncio
async def test_rejects_limit():
    with pytest.raises(ValueError):
        await async_map(lambda x: asyncio.sleep(0, result=x), values(0), 0)

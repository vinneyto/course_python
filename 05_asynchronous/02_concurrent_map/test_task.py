import asyncio

import pytest

from .task import concurrent_map


@pytest.mark.asyncio
async def test_runs_concurrently_and_preserves_order():
    started = set()
    all_started = asyncio.Event()

    async def work(value):
        started.add(value)
        if len(started) == 3:
            all_started.set()
        await asyncio.wait_for(all_started.wait(), timeout=0.2)
        return value * 2

    assert await concurrent_map(work, [3, 1, 2]) == [6, 2, 4]


@pytest.mark.asyncio
async def test_empty_input():
    async def work(value):
        return value

    assert await concurrent_map(work, []) == []

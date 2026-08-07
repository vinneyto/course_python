import asyncio
import inspect

import pytest

from .task import delayed_upper


def test_is_coroutine_function():
    assert inspect.iscoroutinefunction(delayed_upper)


@pytest.mark.asyncio
async def test_waits_cooperatively_and_returns_text():
    task = asyncio.create_task(delayed_upper("hello", 0))
    await asyncio.sleep(0)
    assert await task == "HELLO"

import threading

import pytest

from .task import parallel_map


def test_preserves_order_and_uses_workers():
    barrier = threading.Barrier(2)

    def work(value):
        if value < 2:
            barrier.wait(timeout=2)
        return value * 2

    assert parallel_map(work, iter(range(4)), workers=2) == [0, 2, 4, 6]


def test_validation_and_exception():
    with pytest.raises(ValueError):
        parallel_map(str, [], workers=0)
    with pytest.raises(ZeroDivisionError):
        parallel_map(lambda x: 1 / x, [1, 0, 2])

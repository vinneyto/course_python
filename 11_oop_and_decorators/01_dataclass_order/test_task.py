from dataclasses import FrozenInstanceError

import pytest

from .task import OrderLine


def test_total_defaults_and_ordering():
    apple = OrderLine("apple", 2.5, 2)
    banana = OrderLine("banana", 1.0)

    assert apple.total == 5.0
    assert banana.quantity == 1
    assert sorted([banana, apple]) == [apple, banana]


@pytest.mark.parametrize("args", [("", 1, 1), ("book", -1, 1), ("book", 1, 0)])
def test_rejects_invalid_values(args):
    with pytest.raises(ValueError):
        OrderLine(*args)


def test_is_frozen_and_uses_slots():
    line = OrderLine("book", 10)
    with pytest.raises(FrozenInstanceError):
        line.quantity = 2
    assert not hasattr(line, "__dict__")

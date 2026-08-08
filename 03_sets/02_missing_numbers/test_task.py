import pytest

from .task import missing_numbers


def test_ignores_duplicates_and_values_outside_interval():
    assert missing_numbers([0, 1, 2, 2, 5, 10], 1, 5) == {3, 4}


def test_supports_single_value_interval_and_validates_bounds():
    assert missing_numbers([], 3, 3) == {3}
    assert missing_numbers([3], 3, 3) == set()
    with pytest.raises(ValueError):
        missing_numbers([], 4, 3)

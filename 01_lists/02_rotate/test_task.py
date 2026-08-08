from .task import rotate


def test_rotates_in_both_directions_without_mutating_input():
    items = [1, 2, 3, 4]
    assert rotate(items, 1) == [4, 1, 2, 3]
    assert rotate(items, -1) == [2, 3, 4, 1]
    assert items == [1, 2, 3, 4]


def test_handles_empty_and_large_shifts():
    assert rotate([], 100) == []
    assert rotate([1, 2, 3], 7) == [3, 1, 2]

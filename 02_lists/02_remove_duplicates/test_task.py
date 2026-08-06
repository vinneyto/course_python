from .task import remove_duplicates


def test_removes_duplicates_and_preserves_order():
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_handles_empty_input_and_does_not_mutate_input():
    items = [1, 1]
    assert remove_duplicates(items) == [1]
    assert items == [1, 1]
    assert remove_duplicates([]) == []

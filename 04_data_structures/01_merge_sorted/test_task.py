from itertools import count, islice

from .task import merge_sorted


def test_merges_and_preserves_duplicates():
    assert list(merge_sorted([[1, 4, 4], [], [2, 3, 9]])) == [1, 2, 3, 4, 4, 9]


def test_is_lazy_for_infinite_inputs():
    result = merge_sorted([count(0, 2), count(1, 2)])
    assert list(islice(result, 7)) == list(range(7))

from queue import Queue

from .task import DONE, fan_in


def make_queue(values):
    queue = Queue()
    for value in values:
        queue.put(value)
    queue.put(DONE)
    return queue


def test_merges_all_sources_and_empty_input():
    assert sorted(fan_in([make_queue([1, 3]), make_queue([2, 4])])) == [1, 2, 3, 4]
    assert list(fan_in([])) == []


def test_does_not_confuse_values_with_sentinel():
    assert list(fan_in([make_queue([None, False])])) == [None, False]

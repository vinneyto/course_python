from .task import running_total


def test_yields_running_totals():
    result = running_total([2, -1, 4])
    assert iter(result) is result
    assert list(result) == [2, 1, 5]


def test_empty_input():
    assert list(running_total([])) == []

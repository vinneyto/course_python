from .task import take


def test_takes_requested_number():
    assert take(iter([1, 2, 3, 4]), 2) == [1, 2]


def test_stops_at_end_and_handles_non_positive_count():
    assert take((value for value in [1, 2]), 5) == [1, 2]
    assert take([1, 2], 0) == []
    assert take([1, 2], -1) == []

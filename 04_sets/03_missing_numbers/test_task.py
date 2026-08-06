from .task import missing_numbers


def test_finds_missing_numbers_in_inclusive_range():
    assert missing_numbers([1, 2, 4, 4, 8], 1, 5) == {3, 5}


def test_empty_range():
    assert missing_numbers([1, 2], 5, 3) == set()

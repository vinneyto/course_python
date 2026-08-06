from .task import common_unique


def test_returns_sorted_unique_intersection():
    assert common_unique(["pear", "apple", "pear"], ["pear", "plum", "apple"]) == [
        "apple",
        "pear",
    ]


def test_no_common_values():
    assert common_unique(["a"], ["b"]) == []

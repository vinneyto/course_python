from .task import merge_counters


def test_merges_shared_and_distinct_keys():
    assert merge_counters({"apple": 2, "pear": 1}, {"apple": 3, "plum": 4}) == {
        "apple": 5,
        "pear": 1,
        "plum": 4,
    }


def test_does_not_mutate_inputs():
    left = {"a": 1}
    right = {"a": 2}
    merge_counters(left, right)
    assert left == {"a": 1} and right == {"a": 2}

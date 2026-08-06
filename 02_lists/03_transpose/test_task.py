from .task import transpose


def test_transposes_rectangular_matrix():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_empty_matrix():
    assert transpose([]) == []

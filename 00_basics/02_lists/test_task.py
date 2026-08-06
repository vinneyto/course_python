from .task import positive_squares


def test_filters_squares_and_preserves_order():
    assert positive_squares([-2, 3, 0, 1, 3]) == [9, 1, 9]


def test_does_not_change_input():
    numbers = [2, -1]
    assert positive_squares(numbers) == [4]
    assert numbers == [2, -1]

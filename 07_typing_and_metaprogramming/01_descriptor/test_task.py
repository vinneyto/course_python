import pytest

from .task import Validated


def positive(value: int) -> int:
    if value <= 0:
        raise ValueError("positive required")
    return int(value)


class Product:
    price = Validated(positive)


def test_values_are_independent_and_class_access_works():
    first, second = Product(), Product()
    first.price = 10
    second.price = 20
    assert (first.price, second.price) == (10, 20)
    assert isinstance(Product.price, Validated)


def test_unset_and_invalid_values():
    with pytest.raises(AttributeError):
        _ = Product().price
    with pytest.raises(ValueError):
        Product().price = 0

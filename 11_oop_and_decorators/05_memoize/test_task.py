import pytest

from .task import memoize


def test_caches_arguments_and_normalizes_keyword_order():
    calls = []

    @memoize()
    def multiply(left, right=1):
        calls.append((left, right))
        return left * right

    assert multiply(3, right=4) == 12
    assert multiply(3, **{"right": 4}) == 12
    assert calls == [(3, 4)]
    assert multiply.__name__ == "multiply"


def test_evicts_least_recently_used_entry():
    calls = []

    @memoize(maxsize=2)
    def identity(value):
        calls.append(value)
        return value

    identity(1)
    identity(2)
    identity(1)  # запись 1 снова стала самой свежей
    identity(3)  # должна быть удалена запись 2
    identity(2)
    assert calls == [1, 2, 3, 2]


def test_cache_clear_and_parameter_validation():
    calls = []

    @memoize()
    def answer():
        calls.append(1)
        return 42

    answer()
    answer.cache_clear()
    answer()
    assert len(calls) == 2

    with pytest.raises(ValueError):
        memoize(maxsize=0)

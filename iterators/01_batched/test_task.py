import pytest

from .task import batched


def test_batches_generator_lazily():
    consumed = []
    source = (consumed.append(i) or i for i in range(5))
    result = batched(source, 2)
    assert consumed == []
    assert next(result) == (0, 1) and consumed == [0, 1]
    assert list(result) == [(2, 3), (4,)]


def test_rejects_invalid_size():
    with pytest.raises(ValueError):
        list(batched([], 0))

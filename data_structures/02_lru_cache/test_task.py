import pytest

from .task import LRUCache


def test_eviction_and_refresh():
    cache = LRUCache[str, int](2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    with pytest.raises(KeyError):
        cache.get("b")
    assert len(cache) == 2


def test_update_and_validation():
    with pytest.raises(ValueError):
        LRUCache(0)
    cache = LRUCache(1)
    cache.put("x", 1)
    cache.put("x", 2)
    assert cache.get("x") == 2 and len(cache) == 1

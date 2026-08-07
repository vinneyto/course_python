from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        # TODO: провалидируйте capacity и подготовьте структуру данных.
        raise NotImplementedError

    def get(self, key: K) -> V:
        raise NotImplementedError

    def put(self, key: K, value: V) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

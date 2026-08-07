# LRU-кеш

Реализуйте ограниченный кеш с O(1) `get`/`put`. Чтение и обновление делают ключ
самым свежим; при переполнении вытесняется давно не использованный. `get`
отсутствующего ключа бросает `KeyError`, capacity меньше 1 — `ValueError`.

Не используйте `functools.lru_cache`: здесь важно уметь объяснить структуру.

## Полезные материалы

- [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict) — словарь с операциями изменения порядка элементов; обратите внимание на `move_to_end()` и `popitem()`.
- [Типы отображений — `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) — свойства словаря, на котором можно построить кеш с быстрым поиском.
- [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache) — документация готового LRU-кеша для понимания ожидаемой семантики (но не для использования в решении).

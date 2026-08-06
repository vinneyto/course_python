# Ленивые батчи

Реализуйте генератор `batched(iterable, size)`. Он возвращает кортежи длины
`size`; последний может быть короче. Вход читается только по мере запроса.
При `size <= 0` нужен `ValueError`.

## Полезные материалы

- [Типы итераторов](https://docs.python.org/3/library/stdtypes.html#iterator-types) — протокол `__iter__()` / `__next__()` и поведение исчерпанного итератора.
- [Выражение `yield`](https://docs.python.org/3/reference/expressions.html#yield-expressions) — основа ленивой выдачи батчей.
- [`itertools.batched`](https://docs.python.org/3/library/itertools.html#itertools.batched) — эталонное поведение аналогичной функции и компактная идея реализации.

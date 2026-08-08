# Пропущенные числа

Реализуйте `missing_numbers(values, start, end)`: верните множество целых чисел
из **включительного** диапазона от `start` до `end`, которых нет в `values`.
Повторы и числа за пределами диапазона не влияют на ответ. Если `start > end`,
нужно выбросить `ValueError`.

Пример: `missing_numbers([1, 2, 2, 5, 10], 1, 5) → {3, 4}`.

Запуск: `pytest 03_sets/02_missing_numbers`.

## Полезные материалы

- [`set.difference`](https://docs.python.org/3/library/stdtypes.html#set.difference) — разность множеств.
- [`range`](https://docs.python.org/3/library/stdtypes.html#range) — построение целочисленного диапазона.

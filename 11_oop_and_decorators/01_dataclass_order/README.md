# Строка заказа с `dataclass`

Реализуйте неизменяемый dataclass `OrderLine` с полями `name`, `unit_price` и
`quantity` (по умолчанию `1`). Пустое название, отрицательная цена и количество
меньше единицы должны приводить к `ValueError`. Свойство `total` возвращает
стоимость строки. Включите `slots` и естественную сортировку: сначала по
названию, затем по цене и количеству. `total` не должно участвовать в сравнении.

## Полезные материалы

- [`dataclasses`](https://docs.python.org/3/library/dataclasses.html) — параметры `frozen`, `order` и `slots`, а также `__post_init__`.
- [`property`](https://docs.python.org/3/library/functions.html#property) — вычисляемый атрибут без хранения лишнего состояния.

# Async fan-in

Реализуйте async-генератор `merge(sources)`, объединяющий async iterable по
готовности элементов. Передавайте элемент потребителю сразу, как только его
выдал любой из источников: ожидание следующего элемента от медленного источника
не должно блокировать уже готовые элементы из остальных. При закрытии генератора
отмените созданные задачи; исключение producer должно попасть к consumer,
остальные задачи — завершиться.

## Полезные материалы

- [Асинхронные итераторы](https://docs.python.org/3/reference/expressions.html#asynchronous-generator-functions) — устройство async-генераторов и выдача значений через `yield`.
- [`asyncio.create_task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) — конкурентный запуск корутин и необходимость хранить ссылки на созданные задачи.
- [`asyncio.wait`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait) — ожидание первой завершившейся задачи с `FIRST_COMPLETED`.
- [Отмена задач](https://docs.python.org/3/library/asyncio-task.html#task-cancellation) — распространение `CancelledError` и очистка ресурсов через `try/finally`.

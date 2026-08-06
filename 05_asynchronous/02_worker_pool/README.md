# Асинхронный worker pool

Реализуйте `async_map(fn, items, limit)`. Одновременно работают не более
`limit` awaitable-вызовов, результат сохраняет входной порядок. При первой
ошибке отмените оставшуюся работу. Не создавайте задачу на каждый элемент
заранее: число живых задач должно быть ограничено.

## Полезные материалы

- [`asyncio.Queue`](https://docs.python.org/3/library/asyncio-queue.html) — организация ограниченного числа workers через общую очередь заданий.
- [`asyncio.Semaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore) — альтернативный способ ограничить число одновременно выполняемых корутин.
- [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) — сбор результатов, порядок и поведение при исключениях.
- [Отмена задач](https://docs.python.org/3/library/asyncio-task.html#task-cancellation) — безопасная отмена оставшейся работы после первой ошибки.

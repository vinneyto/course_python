# Первая корутина

Реализуйте `delayed_upper(text, delay)`: асинхронно подождите `delay` секунд и
верните строку в верхнем регистре. Используйте `await asyncio.sleep(delay)`, а
не блокирующий `time.sleep`.

Это вводная задача: одна корутина, одно ожидание, без задач и очередей.
Проследите, что вызов `delayed_upper(...)` сначала создаёт объект корутины, а
выполняет его оператор `await`.

Запуск: `pytest 09_asynchronous/01_first_coroutine`.

## Полезные материалы

- [Корутины и задачи](https://docs.python.org/3/library/asyncio-task.html#coroutines) — синтаксис `async def` и `await`.
- [`asyncio.sleep`](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep) — ожидание, которое отдаёт управление event loop.

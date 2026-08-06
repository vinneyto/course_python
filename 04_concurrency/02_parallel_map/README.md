# Упорядоченный parallel_map

Реализуйте `parallel_map(fn, items, workers)`: выполните работу в пуле потоков,
но верните результаты в порядке входа. Вход может быть генератором. При ошибке
отмените ещё не начатые futures и пробросьте исходное исключение. `workers < 1`
— `ValueError`.

Обсудите: когда потоки ускоряют Python, а когда нужен process pool?

## Полезные материалы

- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) — интерфейсы `Executor`, `Future` и способы ожидания результатов.
- [`Executor.map`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map) — сохранение порядка результатов и отличие `map()` от обработки через `as_completed()`.
- [`Future.cancel`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.cancel) — что именно можно отменить после ошибки и как ведут себя уже запущенные задачи.

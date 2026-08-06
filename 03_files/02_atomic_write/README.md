# Атомарная запись

Создайте контекстный менеджер `atomic_write(path)`. Он отдаёт открытый текстовый
временный файл в той же директории. При успешном выходе файл атомарно заменяет
целевой; при исключении временный удаляется, а старый файл не меняется.

## Полезные материалы

- [Типы контекстных менеджеров](https://docs.python.org/3/library/stdtypes.html#context-manager-types) — контракт методов `__enter__()` и `__exit__()`.
- [`contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) — способ реализовать контекстный менеджер с помощью генератора.
- [`tempfile.NamedTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile) и [`os.replace`](https://docs.python.org/3/library/os.html#os.replace) — создание временного файла рядом с целью и атомарная замена после успешной записи.

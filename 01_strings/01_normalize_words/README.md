# Нормализация строки

Реализуйте `normalize_words(text)`: удалите пробельные символы по краям,
замените любые серии пробельных символов между словами одним пробелом и
приведите строку к нижнему регистру. Знаки препинания менять не нужно.

Примеры: `"  Hello   WORLD " → "hello world"`, пустая строка остаётся пустой.
Попробуйте решить задачу с помощью `str.split()` и `str.join()`.

Запуск: `pytest 01_strings/01_normalize_words`.

## Полезные материалы

- [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split) — разбиение строки с учётом повторяющихся пробелов.
- [`str.join`](https://docs.python.org/3/library/stdtypes.html#str.join) — сборка строки из частей.

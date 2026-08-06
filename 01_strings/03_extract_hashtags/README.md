# Извлечение хештегов

Реализуйте `extract_hashtags(text)`. Разбейте текст по пробельным символам,
выберите части, которые начинаются с `#` и содержат хотя бы один символ после
него, уберите `#` и приведите результат к нижнему регистру. Сохраняйте порядок
и повторы.

Запуск: `pytest 01_strings/03_extract_hashtags`.

## Полезные материалы

- [`str.startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith) — проверка начала строки.
- [Срезы](https://docs.python.org/3/tutorial/introduction.html#strings) — получение части строки без первого символа.

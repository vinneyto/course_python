# Разбор сетевого адреса

Реализуйте `parse_endpoint(value, default_port)`, которая разбирает адрес сервера
и возвращает пару `(host, port)`. Поддержите имена хостов (`example.com:443`),
IPv4 (`127.0.0.1`) и IPv6 в квадратных скобках (`[::1]:8000`). Если порт не
указан, используйте `default_port`. Порт должен быть целым числом от 1 до 65535;
пустой host, лишние двоеточия и IPv6 без скобок должны приводить к `ValueError`.

Запуск: `pytest 09_networking/02_endpoint`.

## Полезные материалы

- [Формат IPv6-литералов в URI](https://datatracker.ietf.org/doc/html/rfc3986#section-3.2.2) — зачем IPv6-адрес заключают в квадратные скобки.
- [`str.rpartition`](https://docs.python.org/3/library/stdtypes.html#str.rpartition) — разделение строки по последнему вхождению разделителя.

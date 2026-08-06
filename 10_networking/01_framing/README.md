# Length-prefixed TCP framing

TCP — поток байтов, один `recv` не обязан совпадать с одним `send`. Реализуйте
`send_message(sock, payload)` и `recv_message(sock, max_size)`. Формат: 4 байта
длины big-endian, затем payload. Отправляйте всё сообщение, дочитывайте ровно
нужное число байт. EOF посреди frame — `EOFError`, слишком большая длина —
`ValueError`; чистый EOF до заголовка возвращает `None`.

## Полезные материалы

- [Практическое руководство по сокетам](https://docs.python.org/3/howto/sockets.html) — почему `send()` и `recv()` обрабатывают лишь часть сообщения и как работать с потоком байтов.
- [`socket.sendall`](https://docs.python.org/3/library/socket.html#socket.socket.sendall) — отправка всех байтов или исключение при ошибке.
- [`int.to_bytes` и `int.from_bytes`](https://docs.python.org/3/library/stdtypes.html#int.to_bytes) — кодирование длины сообщения в четырёхбайтовый big-endian заголовок.

# Length-prefixed TCP framing

TCP — поток байтов, один `recv` не обязан совпадать с одним `send`. Реализуйте
`send_message(sock, payload)` и `recv_message(sock, max_size)`. Формат: 4 байта
длины big-endian, затем payload. Отправляйте всё сообщение, дочитывайте ровно
нужное число байт. EOF посреди frame — `EOFError`, слишком большая длина —
`ValueError`; чистый EOF до заголовка возвращает `None`.


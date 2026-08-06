import socket


def send_message(sock: socket.socket, payload: bytes) -> None:
    # TODO: struct.pack и sendall.
    raise NotImplementedError


def recv_message(sock: socket.socket, max_size: int = 1024 * 1024) -> bytes | None:
    # TODO: вспомогательная функция recv_exact должна учитывать частичные чтения.
    raise NotImplementedError

import socket
import struct

import pytest

from .task import recv_message, send_message


def test_multiple_frames_and_clean_eof():
    left, right = socket.socketpair()
    try:
        send_message(left, b"hello")
        send_message(left, b"")
        left.shutdown(socket.SHUT_WR)
        assert recv_message(right) == b"hello"
        assert recv_message(right) == b""
        assert recv_message(right) is None
    finally:
        left.close()
        right.close()


def test_truncated_and_oversized_frame():
    left, right = socket.socketpair()
    try:
        left.sendall(struct.pack("!I", 10) + b"short")
        left.shutdown(socket.SHUT_WR)
        with pytest.raises(EOFError):
            recv_message(right)
    finally:
        left.close()
        right.close()

    left, right = socket.socketpair()
    try:
        left.sendall(struct.pack("!I", 100))
        with pytest.raises(ValueError):
            recv_message(right, max_size=10)
    finally:
        left.close()
        right.close()

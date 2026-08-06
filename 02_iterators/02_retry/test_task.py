import pytest

from .task import retry


def test_retries_with_backoff_and_preserves_name():
    calls, delays = [], []

    @retry(attempts=3, delay=0.5, backoff=2, sleep=delays.append)
    def unstable():
        calls.append(1)
        if len(calls) < 3:
            raise ValueError("later")
        return 42

    assert unstable() == 42
    assert unstable.__name__ == "unstable"
    assert delays == [0.5, 1.0]


def test_does_not_swallow_unlisted_exception():
    @retry(attempts=5, exceptions=(KeyError,))
    def fail():
        raise TypeError("bad")

    with pytest.raises(TypeError):
        fail()

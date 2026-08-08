import pytest

from .task import count_calls


def test_counts_calls_and_preserves_metadata():
    @count_calls
    def add(left: int, right: int = 1) -> int:
        """Add two numbers."""
        return left + right

    assert add(2, right=3) == 5
    assert add.calls == 1
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."


def test_counts_failed_calls_and_keeps_counters_independent():
    @count_calls
    def fail():
        raise RuntimeError("boom")

    @count_calls
    def succeed():
        return None

    with pytest.raises(RuntimeError):
        fail()
    succeed()

    assert fail.calls == 1
    assert succeed.calls == 1

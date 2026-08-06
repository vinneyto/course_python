import pytest

from .task import tail


def test_tail_handles_unicode_and_final_newline(tmp_path):
    path = tmp_path / "log.txt"
    path.write_text("ноль\nодин\nдва\nтри\n", encoding="utf-8")
    assert tail(path, 2) == ["два", "три"]
    assert tail(path, 20) == ["ноль", "один", "два", "три"]
    assert tail(path, 0) == []


def test_negative_count(tmp_path):
    with pytest.raises(ValueError):
        tail(tmp_path / "unused", -1)

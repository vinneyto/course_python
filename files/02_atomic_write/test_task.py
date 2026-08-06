import pytest

from .task import atomic_write


def test_commits_content(tmp_path):
    target = tmp_path / "data.txt"
    with atomic_write(target) as stream:
        stream.write("готово")
    assert target.read_text() == "готово"


def test_rolls_back_and_cleans_temp_file(tmp_path):
    target = tmp_path / "data.txt"
    target.write_text("old")
    with pytest.raises(RuntimeError):
        with atomic_write(target) as stream:
            stream.write("new")
            raise RuntimeError
    assert target.read_text() == "old"
    assert list(tmp_path.iterdir()) == [target]

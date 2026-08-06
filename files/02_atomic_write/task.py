from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import TextIO


@contextmanager
def atomic_write(path: str | Path, encoding: str = "utf-8") -> Iterator[TextIO]:
    # TODO: tempfile.NamedTemporaryFile + os.replace; гарантируйте cleanup.
    raise NotImplementedError
    yield  # pragma: no cover

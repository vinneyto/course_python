from .task import normalize_words


def test_normalizes_case_and_whitespace():
    assert normalize_words("  Привет,   НОВЫЙ\nМИР!  ") == "привет, новый мир!"


def test_handles_empty_text():
    assert normalize_words(" \t\n ") == ""

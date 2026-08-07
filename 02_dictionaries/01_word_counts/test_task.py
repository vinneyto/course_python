from .task import word_counts


def test_counts_words_ignoring_case():
    assert word_counts(["Python", "code", "PYTHON", "python"]) == {
        "python": 3,
        "code": 1,
    }


def test_empty_input():
    assert word_counts([]) == {}

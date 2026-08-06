from .task import count_vowels


def test_counts_english_and_russian_vowels_ignoring_case():
    assert count_vowels("Hello, Мир!") == 3
    assert count_vowels("АЭРОПОРТ") == 4


def test_text_without_vowels():
    assert count_vowels("123, шшш") == 0

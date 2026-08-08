from .task import extract_hashtags


def test_extracts_unicode_hashtags_and_discards_punctuation():
    assert extract_hashtags("Люблю #Python, #Тесты! И #python_3.") == [
        "python",
        "тесты",
        "python_3",
    ]


def test_ignores_bare_hash_and_keeps_duplicates():
    assert extract_hashtags("#one,#ONE просто # и C#") == ["one", "one"]

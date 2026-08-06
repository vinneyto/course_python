from .task import extract_hashtags


def test_extracts_hashtags_in_order():
    assert extract_hashtags("Учимся #Python и #ASYNC каждый день") == ["python", "async"]


def test_ignores_bare_hash_and_plain_words():
    assert extract_hashtags("обычный текст # без тегов") == []

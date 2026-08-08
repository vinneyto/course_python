from .task import group_anagrams


def test_groups_case_insensitively_and_preserves_spelling():
    words = ["кот", "ток", "сон", "Кто", "нос"]
    assert group_anagrams(words) == [["кот", "ток", "Кто"], ["сон", "нос"]]


def test_accepts_one_pass_iterables_and_empty_words():
    words = (word for word in ["", "a", "", "A"])
    assert group_anagrams(words) == [["", ""], ["a", "A"]]

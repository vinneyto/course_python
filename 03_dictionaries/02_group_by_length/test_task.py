from .task import group_by_length


def test_groups_words_and_preserves_order():
    assert group_by_length(["кот", "я", "дом", "мы"]) == {
        3: ["кот", "дом"],
        1: ["я"],
        2: ["мы"],
    }


def test_empty_input():
    assert group_by_length([]) == {}

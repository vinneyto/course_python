from .task import visitor_stats


def test_returns_all_and_new_visitors():
    assert visitor_stats(["ann", "bob", "ann"], ["bob", "cara"]) == (
        {"ann", "bob", "cara"},
        {"cara"},
    )


def test_empty_days():
    assert visitor_stats([], []) == (set(), set())

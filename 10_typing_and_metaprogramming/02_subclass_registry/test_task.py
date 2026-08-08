import pytest

from .task import Handler


class MessageHandler(Handler):
    pass


class TextHandler(MessageHandler, kind="text"):
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix


def test_registers_and_creates_typed_subclass():
    handler = MessageHandler.create("text", "> ")
    assert isinstance(handler, TextHandler)
    assert handler.prefix == "> "


def test_unknown_and_duplicate_kinds_are_rejected():
    with pytest.raises(KeyError):
        MessageHandler.create("missing")

    with pytest.raises(ValueError):

        class DuplicateTextHandler(MessageHandler, kind="text"):
            pass


def test_direct_subclass_has_an_independent_registry():
    class CommandHandler(Handler):
        pass

    with pytest.raises(KeyError):
        CommandHandler.create("text")

from abc import ABC, abstractmethod
from collections.abc import Iterable


class Notification(ABC):
    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError


class EmailNotification(Notification):
    def __init__(self, recipient: str, subject: str, body: str) -> None:
        # TODO: сохраните необходимые данные.
        raise NotImplementedError

    def render(self) -> str:
        raise NotImplementedError


class SmsNotification(Notification):
    def __init__(self, phone: str, text: str) -> None:
        # TODO: сохраните необходимые данные.
        raise NotImplementedError

    def render(self) -> str:
        raise NotImplementedError


def render_all(notifications: Iterable[Notification]) -> list[str]:
    raise NotImplementedError

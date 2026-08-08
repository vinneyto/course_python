import pytest

from .task import EmailNotification, Notification, SmsNotification, render_all


def test_base_class_is_abstract():
    with pytest.raises(TypeError):
        Notification()


def test_render_all_uses_common_interface():
    notifications = (
        EmailNotification("student@example.com", "Exam", "Tomorrow"),
        SmsNotification("+79990000000", "Done"),
    )

    assert render_all(notifications) == [
        "To: student@example.com | Exam | Tomorrow",
        "SMS +79990000000: Done",
    ]

import pytest

from .task import Temperature


def test_converts_between_scales():
    temperature = Temperature(0)
    assert temperature.fahrenheit == pytest.approx(32)
    assert temperature.kelvin == pytest.approx(273.15)

    temperature.fahrenheit = 212
    assert temperature.celsius == pytest.approx(100)


def test_validates_both_writable_scales():
    with pytest.raises(ValueError):
        Temperature(-273.16)

    temperature = Temperature(20)
    with pytest.raises(ValueError):
        temperature.fahrenheit = -500


def test_kelvin_is_read_only():
    temperature = Temperature(20)
    with pytest.raises(AttributeError):
        temperature.kelvin = 300

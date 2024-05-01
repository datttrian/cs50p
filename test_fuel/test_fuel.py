import pytest
from fuel import convert, gauge


@pytest.mark.parametrize(
    "fraction, expected_percentage",
    [
        ("1/2", 50),
        ("3/4", 75),
        ("2/5", 40),
        ("5/5", 100),
        ("0/10", 0),
        ("10/10", 100),
    ],
)
def test_convert(fraction, expected_percentage):
    assert convert(fraction) == expected_percentage


@pytest.mark.parametrize(
    "percentage, expected_gauge",
    [
        (0, "E"),
        (1, "E"),
        (50, "50%"),
        (99, "F"),
        (100, "F"),
    ],
)
def test_gauge(percentage, expected_gauge):
    assert gauge(percentage) == expected_gauge


def test_invalid_fraction_format():
    with pytest.raises(ValueError):
        convert("invalid")


def test_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("2/1")


def test_denominator_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

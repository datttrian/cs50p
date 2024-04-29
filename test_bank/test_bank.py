from bank import value
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("hello", 0),
        ("Hello there!", 0),
        ("hi", 2),
        ("how are you?", 2),
        ("good morning", 1),
        ("Bye", 1),
        ("HELLO", 0),
        ("hELLo world", 0),
        ("HI EVERYONE", 2),
        ("Greetings", 1),
    ],
)
def test_bank(input_str, expected):
    assert value(input_str) == expected

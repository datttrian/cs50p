from bank import value
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("hello world", 0),
        ("  hello ", 0),
        ("HeLLo", 0),
        ("hi there", 20),
        ("  hey ", 20),
        ("Hullo", 20),
        ("good morning", 100),
        (" yes ", 100),
        ("Ahoy", 100),
    ],
)
def test_bank(input_str, expected):
    assert value(input_str) == expected

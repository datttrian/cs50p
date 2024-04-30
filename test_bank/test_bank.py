from bank import value
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("HeLLo", 0),
        ("hi there", 20),
        ("good morning", 100),
    ],
)
def test_value(input_str, expected):
    assert value(input_str) == expected

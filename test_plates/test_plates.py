from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("ab", True),
        ("abc123", True),
        ("AbCdEf", True),
        ("Aa0bB1", False),
        ("AZ1", True),
        ("ab0", False),
        ("aBcDe1", True),
        ("abc0", False),
        ("abc00", False),
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

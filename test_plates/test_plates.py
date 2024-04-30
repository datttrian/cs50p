from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("abc123", True),
        ("1a2b3c", True),
        ("Tesla3", True),
        ("notValid", False),
        ("abc", False),
        ("12abc", False),
        ("a2b3c", False),
        ("ab0cd", False),
        ("test1234", True),
        ("123456", True),
        ("Python3", True),
        ("@#$%", False),
        ("abc123def", True),
        ("12", False),
        ("ab", False),
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

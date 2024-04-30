from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("", False),  # Invalid: empty string
        ("123", False),  # Invalid: only digits
        ("Ab1234", False),  # Invalid: too many digits
        ("A1", False),  # Invalid: only one letter
        ("A!23", False),  # Invalid: contains a non-alphanumeric character
        ("aB123", False),  # Invalid: lowercase letter
        ("A123B", False),  # Invalid: letters not at the beginning
        ("!Ab123", False),  # Invalid: starts with a non-alphanumeric character
        ("A123B!", False),  # Invalid: ends with a non-alphanumeric character
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

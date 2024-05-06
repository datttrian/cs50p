from plates import is_valid
import pytest

@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("2468", False),  # without beginning alphabetical checks
        ("IRONMAN", False),  # without length checks
        ("ab0123", False),  # without checks for zero placement
        ("xx,.&!", False),  # without checks for alphanumeric characters
        ("xy420z", False),  # without checks for number placement
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

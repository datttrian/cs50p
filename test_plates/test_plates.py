:( test_plates catches plates.py without beginning alphabetical checks
    expected exit code 1, not 0
:( test_plates catches plates.py without length checks
    expected exit code 1, not 0


from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        (
            "Ab123",
            True,
        ),  # Valid: starts with two letters, followed by non-zero leading digits
        ("Ab012", False),  # Invalid: has zero as first digit
        ("Ab12a3", False),  # Invalid: digits not contiguous or non-digit after digit
        ("Ab", True),  # Valid: just two letters, no digits
        ("AB1", True),  # Valid: starts with two letters, followed by a non-zero digit
        ("ABCD", True),  # Valid: alphabetic within valid length
        ("AB!", False),  # Invalid: contains a non-alphanumeric character
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

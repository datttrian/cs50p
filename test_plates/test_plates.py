from plates import is_valid
import pytest

@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        # ("2468", False),  # without beginning alphabetical checks
        # ("IRONMAN", False),  # without length checks
        ("ab0123", False),  # without checks for zero placement
        ("xx,.&!", False),  # without checks for alphanumeric characters
        ("xy420z", False),  # without checks for number placement
        # ("ON1123", True),  # length and number placement checks
        # ("hadley", True),  # beginning alphabetical checks
        # ("dddd", True),  # beginning alphabetical checks
        # ("AsLongAsYouLoveMe", False),  # length checks
        # ("c", False),  # length checks
        # ("CS15", True),  # length checks and alphanumeric character checks
        # ("abc69xyz", False),  # alphanumeric character checks
        # ("cs50p", False),  # alphanumeric character checks
        # ("bl <42>", False),  # checks for alphanumeric characters
        # ("07bond", False),  # checks for zero placement and number placement
        # ("c1ix", False),  # alphanumeric character checks and length checks
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

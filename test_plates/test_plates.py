from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("ON1123", True),  # length and number placement checks
        ("hadley", True),  # beginning alphabetical checks
        ("dddd", True),  # beginning alphabetical checks
        ("AsLongAsYouLoveMe", False),  # length checks
        ("c", False),  # length checks
        ("2468", False),  # length checks
        ("IRONMAN", False),  # length checks
        ("CS15", True),  # length checks and alphanumeric character checks
        ("abc69xyz", False),  # alphanumeric character checks
        ("cs50p", False),  # alphanumeric character checks
        (
            "ab0123",
            False,
        ),  # checks for zero placement and alphanumeric character checks
        ("xx,.&!", False),  # checks for alphanumeric characters
        ("bl <42>", False),  # checks for alphanumeric characters
        ("07bond", False),  # checks for zero placement and number placement
        ("xy420z", False),  # alphanumeric character checks and number placement
        ("c1ix", False),  # alphanumeric character checks and length checks
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

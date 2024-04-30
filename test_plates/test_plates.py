from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("ON1123", True),
        ("hadley", True),
        ("AsLongAsYouLoveMe", False),
        ("c", False),
        ("abc69xyz", False),
        ("cs50p", False),
        ("ab0123", False),
        ("xy420z", False),
        ("mnp,!&.", False),
        ("bl <42>", False),
        ("07bond", False),
        ("c1ix", False),
        ("dddd", True),
        ("2468", False),
        ("IRONMAN", False),
        ("CS15", True),
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

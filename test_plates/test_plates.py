from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("NeverGonnaGiveYouUp", False),
        ("IAMGROOT", False),
        ("x", False),
        ("cs50p", False),
        ("xx <42>", False),
        ("ab69cd", False),
        ("ab0123", False),
        ("xy420z", False),
        ("xx,.&!", False),
        ("07bond", False),
        ("8055", False),
        ("IN1947", True),
        ("mbappe", True),
        ("rr", True),
        ("CS1337", True),
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

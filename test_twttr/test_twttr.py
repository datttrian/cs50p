from twttr import shorten
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("bcdfg", "bcdfg"),  # without vowel replacement
        ("Python 3.9", "Pythn 3.9"),  # mixed letters and numbers
        ("", ""),  # an empty string
        ("Hey! How are you?", "Hy! Hw r y?"),  # punctuation included
        ("beautiful", "btfl"),  # all lowercase vowels present in the input
    ],
)
def test_isAnagram(input_str, expected):
    assert shorten(input_str) == expected

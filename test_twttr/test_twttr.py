from twttr import shorten
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("bcdfg", "bcdfg"),
        ("aeiouAEIOU", ""),
        ("Hello World", "Hll Wrld"),
        ("Python 3.9", "Pythn 3.9"),
        ("", ""),
        ("Hey! How are you?", "Hy! Hw r y?"),
        ("beautiful", "btfl"),
    ],
)
def test_isAnagram(input_str, expected):
    assert shorten(input_str) == expected

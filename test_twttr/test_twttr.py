from twttr import shorten
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("aeiouAEIOU", ""),
        ("Python 3.9", "Pythn 3.9"),
        # ("bcdfg", "bcdfg"),
        # ("Hello World", "Hll Wrld"),
        # ("", ""),
        # ("Hey! How are you?", "Hy! Hw r y?"),
        # ("beautiful", "btfl"),
    ],
)
def test_shorten(input_str, expected):
    assert shorten(input_str) == expected

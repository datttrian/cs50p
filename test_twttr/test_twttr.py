from twttr import shorten
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("Python 3.9", "Pythn 3.9"),  # omitting numbers, printing in uppercase, omitting punctuation
    ],
)
def test_shorten(input_str, expected):
    assert shorten(input_str) == expected

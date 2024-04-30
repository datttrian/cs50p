from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("ab12", True),
        ("123ab", False),
        ("ab12!", False),
        ("a", False),
        ("abcdefg", False),
        ("ab", False),
        ("ab123cd", False),
        ("ab0123", False),
    ],
)
def test_twttr(input_str, expected):
    assert is_valid(input_str) == expected

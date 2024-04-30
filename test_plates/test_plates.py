from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("ab1", True),
        ("XY12", True),
        ("Te123", True),
        ("Z9", True),
        ("ab12", True),
        ("1xy", False),
        ("abc", False),
        ("a0b1", False),
        ("xy-12", False),
        ("XYZ1234", False),
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

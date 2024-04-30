from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("Abcd12", True),
        ("Ab", False),
        ("Abcdef", True),
        ("Abc12$", False),
        ("Abcd12", True),
        ("Ab", False),
        ("Abcdef", True),
        ("Abc12$", False),
        ("Abcd123", True),
        ("AbcdEf", False),
        ("12345", False),
        ("123abc", False),
        ("Ab#$12", False),
        ("Ab1234", True),
        ("Abc123e", True),
        ("Abc012", False),
        ("", False),
        ("A@3", False),
        ("Abc07", False),
        ("Aa123", True),
        ("AbcdEf", False),
        ("12345", False),
        ("123abc", False),
        ("Ab#$12", False),
        ("Ab1234", True),
        ("Abc123e", True),
        ("Abc012", False),
        ("", False),
        ("A@3", False),
        ("Abc07", False),
        ("Aa123", True),
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

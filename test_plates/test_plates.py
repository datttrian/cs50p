from plates import is_valid
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("Abcd12", True),
        ("Abc12$", False),
        ("Abcd12", True),
        ("Abc12$", False),
        ("Ab#$12", False),
        ("Ab1234", True),
        ("Abc012", False),
        ("Abc07", False),
        ("Aa123", True),
        ("AbcdEf", True),
        ("Ab#$12", False),
        ("Ab1234", True),
        ("Abc012", False),
        ("Abc07", False),
        ("Aa123", True),
    ],
)
def test_is_valid(input_str, expected):
    assert is_valid(input_str) == expected

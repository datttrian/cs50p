from um import count
import pytest


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("Um", 1),
        ("Um um um", 3),
        ("No ums here", 0),
        ("This is an umbrella", 0),
        ("Crumb", 0),
        ("uM uM uM", 3),
    ],
)
def test_count(input_str, expected):
    assert count(input_str) == expected

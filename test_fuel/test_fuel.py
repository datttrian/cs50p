import pytest
from fuel import convert, gauge

def test_convert_valid_input():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("0/5") == 0

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("abc/def")
    with pytest.raises(ValueError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("2.5/4")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

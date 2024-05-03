from working import convert
import pytest

def test_valid_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("9:00 PM to 5:30 AM") == "21:00 to 05:30"

def test_invalid_formats():
    with pytest.raises(ValueError):
        assert convert("9:00 AM lol 5:30 PM")

def test_invalid_times():
    with pytest.raises(ValueError):
        assert convert("13:00 AM to 69:30 PM")

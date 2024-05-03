from working import convert
import pytest

def test_valid_formats():
    # Test valid input formats
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:30 AM to 1:45 PM") == "00:30 to 13:45"
    assert convert("11 AM to 12 PM") == "11:00 to 12:00"
    assert convert("1:30 PM to 3:45 PM") == "13:30 to 15:45"

def test_invalid_formats():
    # Test invalid input formats
    with pytest.raises(ValueError):
        convert("9:00 AM to 5 PM")  # Missing minute in first time
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")  # Wrong delimiter
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")  # Invalid hour in second time
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid hour in first time
    with pytest.raises(ValueError):
        convert("15:30 PM to 6:45 AM")  # Inconsistent AM/PM in times

def test_invalid_times():
    # Test invalid times
    with pytest.raises(ValueError):
        convert("13:60 AM to 5:00 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("12:30 AM to 25:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("12:30 AM to 5:70 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("12:30 AM to 5:00 PP")  # Invalid AM/PM

if __name__ == "__main__":
    pytest.main(["-v", "test_working.py"])

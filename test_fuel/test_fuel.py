import pytest
from fuel import convert, gauge

# Test cases for the convert function
def test_convert_valid_fraction():
    assert convert("3/4") == 75  # 3/4 as a percentage is 75%

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")  # X is greater than Y, should raise ValueError

def test_convert_non_integer_input():
    with pytest.raises(ValueError):
        convert("2.5/3")  # Non-integer input, should raise ValueError

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")  # Denominator is 0, should raise ZeroDivisionError

# Test cases for the gauge function
def test_gauge_e():
    assert gauge(1) == "E"  # Percentage is 1, should return "E"

def test_gauge_f():
    assert gauge(99) == "F"  # Percentage is 99, should return "F"

def test_gauge_between_1_and_99():
    assert gauge(50) == "50%"  # Percentage is between 1 and 99, should return "50%"

if __name__ == "__main__":
    pytest.main()

# test_fuel.py

import fuel

def test_convert():
    # Test valid input
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/2") == 50

    # Test X is greater than Y
    try:
        fuel.convert("4/3")
    except ValueError as e:
        assert str(e) == "X is greater than Y"

    # Test Y is 0
    try:
        fuel.convert("2/0")
    except ZeroDivisionError as e:
        assert str(e) == "Y cannot be 0"

    # Test invalid input format
    try:
        fuel.convert("invalid")
    except ValueError as e:
        assert str(e) == "Invalid input. Please enter a fraction in the format X/Y where X and Y are integers."

def test_gauge():
    # Test E
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"

    # Test F
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"

    # Test Z%
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(75) == "75%"

    # Test invalid input
    try:
        fuel.gauge("invalid")
    except ValueError as e:
        assert str(e) == "Invalid input. Please provide a valid percentage as an integer."

if __name__ == "__main__":
    import pytest
    pytest.main()

import plates

# Test cases for the is_valid function
def test_valid_plate():
    assert plates.is_valid("AB1234") == True

def test_invalid_length():
    assert plates.is_valid("A") == False
    assert plates.is_valid("ABCDEFGH") == False

def test_non_alphabetic_start():
    assert plates.is_valid("123ABC") == False
    assert plates.is_valid("12AB34") == False

def test_non_alphanumeric():
    assert plates.is_valid("AB#123") == False
    assert plates.is_valid("AB!123") == False

def test_invalid_digits():
    assert plates.is_valid("AB0000") == False
    assert plates.is_valid("AB0123C") == False

def test_valid_zero_digits():
    assert plates.is_valid("AB01234") == True
    assert plates.is_valid("AB0") == True

if __name__ == "__main__":
    # Run the tests using pytest
    import pytest
    pytest.main()

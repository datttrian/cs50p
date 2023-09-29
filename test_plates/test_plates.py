import plates

def test_is_valid_plate():
    assert plates.is_valid("AB1234") == True

def test_is_invalid_length():
    assert plates.is_valid("ABC") == False

def test_is_non_alphabetic_characters():
    assert plates.is_valid("123456") == False

def test_is_non_alphanumeric_characters():
    assert plates.is_valid("AB$123") == False

def test_is_non_alpha_start():
    assert plates.is_valid("123AB4") == False

def test_is_contains_zero():
    assert plates.is_valid("AB0123") == False

def test_is_valid_single_digit():
    assert plates.is_valid("A1B23C") == True

def test_is_valid_long_plate():
    assert plates.is_valid("ABCDE12345") == True

def test_is_invalid_long_plate():
    assert plates.is_valid("ABCDEFG12345") == False

if __name__ == "__main__":
    test_is_valid_plate()
    test_is_invalid_length()
    test_is_non_alphabetic_characters()
    test_is_non_alphanumeric_characters()
    test_is_non_alpha_start()
    test_is_contains_zero()
    test_is_valid_single_digit()
    test_is_valid_long_plate()
    test_is_invalid_long_plate()
    print("All tests passed!")

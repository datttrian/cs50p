from plates import is_valid


# All vanity plates must start with at least two letters
def test_begintwoletters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False

# ... vanity plates may contain a maximum of 6 characters (letters or numbers) and a 


from numb3rs import validate


def test_valid_ipv4():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True


def test_invalid_ipv4():
    assert validate("275.3.6.28") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False

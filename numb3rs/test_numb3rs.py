import pytest
from numb3rs import validate


def test_valid_ipv4():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True


def test_invalid_ipv4():
    assert validate("256.255.255.255") == False  # Value greater than 255
    assert validate("64.128.256.512") == False  # Value greater than 255
    assert validate("8.8.8") == False  # Incomplete address
    assert validate("10.10.10.10.10") == False  # More than four bytes


def test_edge_cases():
    assert validate("0.0.0.0") == True  # Lowest possible address
    assert validate("255.255.255.254") == True  # Highest possible address, excluding broadcast
    assert validate("255.255.255.255") == True  # Highest possible address, including broadcast


if __name__ == "__main__":
    pytest.main()

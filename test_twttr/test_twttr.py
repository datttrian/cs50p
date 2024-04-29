from twttr import shorten
import pytest

def test_no_vowels():
    assert shorten("bcdfg") == "bcdfg", "Should return the same string if no vowels"

def test_all_vowels():
    assert shorten("aeiouAEIOU") == "", "Should return an empty string if all characters are vowels"

def test_mixed_case():
    assert shorten("Hello World") == "Hll Wrld", "Should correctly remove both uppercase and lowercase vowels"

def test_with_numbers():
    assert shorten("Python 3.9") == "Pythn 3.9", "Should return string with numbers intact but vowels removed"

def test_empty_string():
    assert shorten("") == "", "Should return an empty string if input is empty"

def test_special_characters():
    assert shorten("Hey! How are you?") == "Hy! Hw r y?", "Should handle strings with special characters and spaces"

def test_continuous_vowels():
    assert shorten("beautiful") == "btfl", "Should handle words with continuous vowels"

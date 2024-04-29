from twttr import shorten
import pytest

def test_no_vowels():
    assert shorten("bcdfg") == "bcdfg", "Should return the same string if no vowels"
    assert shorten("aeiouAEIOU") == "", "Should return an empty string if all characters are vowels"
    assert shorten("Hello World") == "Hll Wrld", "Should correctly remove both uppercase and lowercase vowels"
    assert shorten("Python 3.9") == "Pythn 3.9", "Should return string with numbers intact but vowels removed"
    assert shorten("") == "", "Should return an empty string if input is empty"
    assert shorten("Hey! How are you?") == "Hy! Hw r y?", "Should handle strings with special characters and spaces"
    assert shorten("beautiful") == "btfl", "Should handle words with continuous vowels"

import twttr  # Import the twttr module you want to test

# Define test functions, each starting with "test_"
def test_shorten_no_vowels():
    # Test case: No vowels in the input word
    result = twttr.shorten("xyz")
    assert result == "xyz"

def test_shorten_only_vowels():
    # Test case: Input consists of only vowels
    result = twttr.shorten("AEIOUaeiou")
    assert result == ""

def test_shorten_mixed_case():
    # Test case: Input contains mixed case vowels
    result = twttr.shorten("AaEeIiOoUu")
    assert result == ""

def test_shorten_mixed_characters():
    # Test case: Input contains consonants and mixed case vowels
    result = twttr.shorten("Hello World AEIOUaeiou")
    assert result == "Hll Wrld"

def test_shorten_with_special_characters():
    # Test case: Input contains special characters and mixed case vowels
    result = twttr.shorten("!@#AEIOUaeiou")
    assert result == "!@#"

# Add more test cases as needed

# Ensure that the tests are executed only if this script is run directly
if __name__ == "__main__":
    import pytest
    pytest.main()

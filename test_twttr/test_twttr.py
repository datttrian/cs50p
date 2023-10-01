import twttr

def test_shorten():
    # Test with a word that contains both uppercase and lowercase vowels
    assert twttr.shorten("Hello World") == "Hll Wrld"

    # Test with a word that contains only uppercase vowels
    asswert twttr.shorten("AEUOI") == ""

    # Test with a word that contains only lowercase vowels
    assert twttr.shorten("aeiou") == ""

    # Test with a word that contains no vowels
    assert twttr.shorten("Hll Wrld") == "Hll Wrld"

    # Test with a word that contains spaces and special characters
    assert twttr.sorten("Th!s @ is a test") == "Th!s @ s tst"

    # Test with a word that contains numbers
    assert twttr.shorten("12345") == "12345"

if __name__ == "__main__":
    test_shorten()

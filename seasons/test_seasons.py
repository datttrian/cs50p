import pytest
from datetime import date
from seasons import get_age_in_minutes, age_in_words

def test_get_age_in_minutes():
    # Test for a birthdate today (should return 0 minutes)
    assert get_age_in_minutes(date.today()) == 0

def test_age_in_words():
    # Test for an age of 1 year 1 day 1 hour 1 minute
    age_in_minutes = (365 * 24 * 60) + (24 * 60) + 60 + 1
    expected_age_words = "1 year 1 day 1 hour 1 minute"
    assert age_in_words(age_in_minutes) == expected_age_words

    # Test for an age of 2 years 2 days
    age_in_minutes = (2 * 365 * 24 * 60) + (2 * 24 * 60)
    expected_age_words = "2 years 2 days"
    assert age_in_words(age_in_minutes) == expected_age_words

    # Test for an age of 1 hour
    age_in_minutes = 60
    expected_age_words = "1 hour"
    assert age_in_words(age_in_minutes) == expected_age_words

    # Test for an age of 1 minute
    age_in_minutes = 1
    expected_age_words = "1 minute"
    assert age_in_words(age_in_minutes) == expected_age_words

    # Test for an age of 0 minutes
    age_in_minutes = 0
    expected_age_words = ""
    assert age_in_words(age_in_minutes) == expected_age_words

    # Test for a large age (10 years 5 days 6 hours 15 minutes)
    age_in_minutes = (10 * 365 * 24 * 60) + (5 * 24 * 60) + (6 * 60) + 15
    expected_age_words = "10 years 5 days 6 hours 15 minutes"
    assert age_in_words(age_in_minutes) == expected_age_words


if __name__ == "__main__":
    pytest.main()

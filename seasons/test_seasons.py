from seasons import parse_date, minutes_difference, number_to_words
import pytest
from datetime import date

def test_parse_date():
    assert parse_date("2023-05-01") == date(2023, 5, 1)
    with pytest.raises(SystemExit):
        parse_date("2023-02-30")

def test_minutes_difference():
    assert minutes_difference(date(2023, 1, 1), date(2023, 1, 2)) == 1440

def test_number_to_words():
    assert number_to_words(1440) == "one thousand, four hundred forty"
    assert number_to_words(525600) == "five hundred twenty-five thousand, six hundred"

# Configure the pytest command to run these tests:
# pytest test_seasons.py

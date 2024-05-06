import pytest
from datetime import date
from seasons import get_total_minutes


@pytest.mark.parametrize(
    ("start_date", "end_date", "expected_minutes"),
    [
        (date(1999, 1, 1), date(2000, 1, 1), 525600),
        (date(2000, 1, 1), date(2012, 1, 1), 6311520),
        (date(2024, 2, 29), date(2024, 5, 1), 89280),
        (date(2024, 1, 1), date(2033, 1, 1), 4734720),
    ],
)
def test_get_minutes(start_date, end_date, expected_minutes):
    assert get_total_minutes(start_date, end_date) == expected_minutes

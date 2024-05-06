from datetime import date, datetime
import sys
from inflect import engine

def main():
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.combine(date.today(), datetime.min.time())
        if dob > today:
            raise ValueError("Date of birth cannot be in the future.")
        age_in_minutes = calculate_age_in_minutes(dob, today)
        age_in_words = convert_minutes_to_words(age_in_minutes)
        print(f"You are {age_in_words} minutes old.")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        sys.exit(1)

def calculate_age_in_minutes(start, end):
    delta = end - start
    return round(delta.total_seconds() / 60)

def convert_minutes_to_words(minutes):
    p = engine()
    words = p.number_to_words(minutes).replace("-", " ").replace(",", "")
    return words

if __name__ == "__main__":
    main()

from datetime import date
import sys

def age_in_minutes(birth_date):
    today = date.today()
    age_in_days = (today - birth_date).days
    age_in_minutes = age_in_days * 24 * 60
    return age_in_minutes

def convert_to_words(minutes):
    # Define the words for numbers from one to nineteen
    num_words = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    # Define the words for tens
    tens_words = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    if minutes == 0:
        return "zero"

    if minutes < 20:
        return num_words[minutes]

    if minutes < 100:
        return tens_words[minutes // 10] + num_words[minutes % 10]

    # Divide minutes into years, days, hours, and minutes
    years = minutes // (365 * 24 * 60)
    minutes %= (365 * 24 * 60)
    days = minutes // (24 * 60)
    minutes %= (24 * 60)
    hours = minutes // 60
    minutes %= 60

    # Convert each part into words
    years_str = convert_to_words(years) + " million" if years > 1 else " million" if years == 1 else ""
    days_str = convert_to_words(days) + " thousand" if days > 1 else " thousand" if days == 1 else ""
    hours_str = convert_to_words(hours)
    minutes_str = convert_to_words(minutes)

    # Construct the final string
    result = years_str + days_str + hours_str + minutes_str + " minutes"
    return result.strip()

def main():
    try:
        # Get user input
        birth_date_str = input("Date of Birth (YYYY-MM-DD): ")

        # Convert input string to date object
        birth_date = date.fromisoformat(birth_date_str)

        # Calculate age in minutes
        age_minutes = age_in_minutes(birth_date)

        # Convert age in minutes to words and print
        print(convert_to_words(age_minutes))

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

if __name__ == "__main__":
    main

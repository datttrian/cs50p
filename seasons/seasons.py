from datetime import datetime, date
import sys

def get_age_in_minutes(birthdate):
    today = date.today()
    age_in_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_in_minutes = age_in_years * 365 * 24 * 60
    return age_in_minutes

def age_in_words(age_in_minutes):
    years = age_in_minutes // (365 * 24 * 60)
    remainder = age_in_minutes % (365 * 24 * 60)
    days = remainder // (24 * 60)
    hours = (remainder % (24 * 60)) // 60
    minutes = remainder % 60

    age_words = ""
    if years > 0:
        age_words += f"{years} year"
        if years != 1:
            age_words += "s"
    if days > 0:
        age_words += f" {days} day"
        if days != 1:
            age_words += "s"
    if hours > 0:
        age_words += f" {hours} hour"
        if hours != 1:
            age_words += "s"
    if minutes > 0:
        age_words += f" {minutes} minute"
        if minutes != 1:
            age_words += "s"

    return age_words.strip()

def main():
    user_input = input("Please enter your date of birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        sys.exit(1)

    age_in_minutes = get_age_in_minutes(birthdate)
    age_words = age_in_words(age_in_minutes)

    print(f"You are {age_words} old in minutes.")

if __name__ == "__main__":
    main()

from datetime import date
import inflect
import sys


def get_total_minutes(birth_date, today):
    # Calculate the difference in days and convert it to minutes
    return (today - birth_date).days * 24 * 60


def main():
    # Prompt the user for their date of birth in YYYY-MM-DD
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        # Exit the program if the input date is invalid
        sys.exit("Invalid date")

    # Calculate total minutes lived since the given birth date
    total_minutes = get_total_minutes(birth_date, date.today())
    p = inflect.engine()

    # Print the total minutes in word form with proper pluralization
    print(
        f"{p.number_to_words(total_minutes, andword='').capitalize()} {p.plural('minute', total_minutes)}"
    )


if __name__ == "__main__":
    main()

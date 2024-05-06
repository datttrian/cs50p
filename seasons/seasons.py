from datetime import date
import sys
import inflect

def parse_date(input_date):
    try:
        year, month, day = map(int, input_date.split('-'))
        return date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

def minutes_difference(birth_date, current_date):
    time_delta = current_date - birth_date
    return time_delta.days * 24 * 60  # Days to minutes

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="")

def main():
    user_input = input("Date of Birth: ")
    birth_date = parse_date(user_input)
    current_date = date.today()
    minutes = minutes_difference(birth_date, current_date)
    print(number_to_words(minutes))

if __name__ == "__main__":
    main()

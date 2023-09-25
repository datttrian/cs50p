# List of month names
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def validate_date(input_date):
    parts = input_date.split()  # Split the input by whitespace

    if len(parts) == 3:
        month = parts[0]
        day = parts[1].strip(",")
        year = parts[2]

        if month in months:
            try:
                day = int(day)
                year = int(year)
                if 1 <= day <= 31 and 0 <= year <= 9999:
                    return f"{year:04d}-{months.index(month) + 1:02d}-{day:02d}"
            except ValueError:
                pass

    elif len(parts) == 1:
        date_parts = parts[0].split("/")
        if len(date_parts) == 3:
            try:
                month = int(date_parts[0])
                day = int(date_parts[1])
                year = int(date_parts[2])
                if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 9999:
                    return f"{year:04d}-{month:02d}-{day:02d}"
            except ValueError:
                pass

    return None


def main():
    while True:
        user_input = input("Date: ")
        converted_date = validate_date(user_input)

        if converted_date:
            print(converted_date)
            break
        else:
            print("Invalid date. Please enter a valid date in the specified formats.")


if __name__ == "__main__":
    main()

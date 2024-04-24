months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def is_valid_date(date_str):
    try:
        parts = date_str.split('/')
        if len(parts) == 3:
            month, day, year = parts
            month = month.strip()
            day = day.strip()
            year = year.strip()
            if month.isdigit() and day.isdigit() and year.isdigit():
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return True
    except ValueError:
        pass
    return False


def format_date(date_str):
    parts = date_str.split('/')
    month, day, year = parts
    month = month.strip()
    day = day.strip()
    year = year.strip()

    if month.isdigit():
        month = int(month)
        month = months[month - 1]

    return f"{year}-{month:02d}-{day:02d}"


while True:
    date_input = input("Date: ")
    if is_valid_date(date_input):
        formatted_date = format_date(date_input)
        print(formatted_date)
        break
    else:
        print("Invalid date format. Please try again.")

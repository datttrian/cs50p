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

while True:
    user_input = input("Date: ")

    # Try to split the input into parts
    date_parts = user_input.split()

    # Check if there are at least 3 parts
    if len(date_parts) >= 3:
        # Extract month, day, and year
        month = date_parts[0]
        day = date_parts[1].strip(",")
        year = date_parts[2]

        # Check if month is valid
        if month in months:
            # Try to convert day and year to integers
            try:
                day = int(day)
                year = int(year)
            except ValueError:
                pass
            else:
                # Check if day and year are within reasonable ranges
                if 1 <= day <= 31 and 1 <= year <= 9999:
                    # Convert month to its numeric representation (1-12)
                    month_number = months.index(month) + 1

                    # Format the date as YYYY-MM-DD
                    formatted_date = f"{year:04d}-{month_number:02d}-{day:02d}"
                    print(formatted_date)
                    break

    print("Invalid date. Please enter a valid date in month-day-year format.")

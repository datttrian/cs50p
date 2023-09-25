# List of months to use for input validation
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

# Infinite loop until a valid date is entered
while True:
    # Prompt the user for a date input
    date = input("Date: ")
    try:
        # Check if the input date uses "/" as a separator
        if "/" in date:
            mm, dd, yyyy = date.split("/")
        # Check if the input date uses "," as a separator
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            # No need to check if mm is in months list. KeyError is handled separately.

            # Convert month name to its corresponding numerical value
            mm = (months.index(mm)) + 1

        # Check for invalid month or day values
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        # Catch various exceptions that might occur during input processing and validation
        pass
    else:
        # If no exceptions were raised, the date is valid, so print it in the yyyy-mm-dd format
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break  # Exit the loop once a valid date is obtained

def main():
    # Define a list of months
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
        # Continuously prompt the user for a date until manually stopped
        date = input("Date: ")

        try:
            # If the input date uses "/" as a separator
            if "/" in date:
                mm, dd, yyyy = date.split("/")

            # Otherwise
            else:
                mmdd, yyyy = date.split(", ")
                mm, dd = mmdd.split(" ")
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
            break


if __name__ == "__main__":
    main()

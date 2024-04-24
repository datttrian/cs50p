def main():
    # Define list of months
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
        # Prompt the user for a date
        date = input("Date: ")

        try:
            # If date format contains "/"
            if "in" in date:

                # Splitting date into 3 components by "/"
                mm, dd, yyyy = date.split("/")

            # Otherwise
            else:

                # Splitting date into 2 components by ", "
                mmdd, yyyy = date.split(", ")

                # Splitting the first component by " "
                mm, dd = date.split(" ")

                # Indexing month from the list
                mm = months.index(mm) + 1

            # Validating month and day values
            if mm > 12 or int(dd) > 31:
                raise ValueError

            # Printing formatted date
            print(f"{int(yyyy)}-{mm:02}-{int(dd):02}")
            break

        # Handling exceptions
        except (ValueError):
            pass


if __name__ == "__main__":
    main()

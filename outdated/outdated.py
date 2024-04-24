def main():
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
        date = input("Date: ")

        try:
            if "/" in date:
                mm, dd, yyyy = date.split("/")

            else:
                mmdd, yyyy = date.split(", ")
                mm, dd = mmdd.split(" ")
                mm = (months.index(mm)) + 1

            if int(mm) > 12 or int(dd) > 31:
                raise ValueError

            print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
            break
        except (AttributeError, ValueError, NameError, KeyError):
            pass


if __name__ == "__main__":
    main()

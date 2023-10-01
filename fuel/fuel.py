def get_fuel_percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split("/"))

            if y == 0 or x > y or x < 0:
                raise ValueError

            percentage = (x / y) * 100

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction (X/Y).")


if __name__ == "__main__":
    main()

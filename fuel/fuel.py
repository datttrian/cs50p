def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split("/"))
            if x <= y and y > 0:
                return x, y
            else:
                print("Invalid fraction. Please try again.")
        except (ValueError, ZeroDivisionError):
            print(
                "Invalid input. Please enter a fraction in the format X/Y where X and Y are integers."
            )


def calculate_fuel_percentage(x, y):
    percentage = (x / y) * 100
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(round(percentage)) + "%"


def main():
    x, y = get_fraction()
    result = calculate_fuel_percentage(x, y)
    print(result)


if __name__ == "__main__":
    main()

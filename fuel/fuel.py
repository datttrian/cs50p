def calculate_fuel_percentage(fraction):
    try:
        numerator, denominator = map(int, fraction.split("/"))
        if numerator > denominator or denominator == 0:
            raise ValueError
        percentage = (numerator / denominator) * 100
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(round(percentage)) + "%"
    except (ValueError, ZeroDivisionError):
        return None


def main():
    while True:
        fraction = input("Fraction: ")
        result = calculate_fuel_percentage(fraction)
        if result is not None:
            print(result)
            break
        else:
            print("Invalid input. Please enter a valid fraction.")


if __name__ == "__main__":
    main()

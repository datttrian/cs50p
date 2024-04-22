def get_fuel_percentage(fraction_str):
    try:
        # Split the fraction string into numerator and denominator
        numerator, denominator = map(int, fraction_str.split('/'))

        # Check if denominator is zero or numerator is greater than denominator
        if denominator == 0 or numerator > denominator:
            raise ValueError

        # Calculate fuel percentage
        percentage = numerator / denominator * 100

        # Round percentage to the nearest integer
        rounded_percentage = round(percentage)

        # Check if tank is essentially empty or full
        if rounded_percentage <= 1:
            return 'E'
        elif rounded_percentage >= 99:
            return 'F'
        else:
            return f'{rounded_percentage}%'

    except (ValueError, ZeroDivisionError):
        # Prompt the user again if input is invalid
        print("Invalid input. Please enter a valid fraction (X/Y), where X and Y are integers and Y is not zero.")
        fraction_str = input("Fraction: ")
        return get_fuel_percentage(fraction_str)


if __name__ == "__main__":
    fraction_str = input("Fraction: ")
    fuel_percentage = get_fuel_percentage(fraction_str)
    print(fuel_percentage)

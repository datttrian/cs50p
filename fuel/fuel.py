def get_fuel_percentage(fraction_str):
    try:
        # Split the fraction string into numerator and denominator
        numerator, denominator = map(int, fraction_str.split('/'))

        # Catch exception ValueError
        if denominator == 0 or numerator > denominator:
            raise ValueError

        # Calculate fuel percentage
        percentage = numerator / denominator * 100

        # Round percentage to the nearest integer

        # Check if tank is essentially empty or full

        # Prompt the user again if input is invalid


if __name__ == "__main__":
    fraction_str = input("Fraction: ")
    fuel_percentage = get_fuel_percentage(fraction_str)
    print(fuel_percentage)

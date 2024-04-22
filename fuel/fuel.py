def get_fuel_percentage(fraction_str):
    try:
        # Split the fraction string into numerator and denominator
        numerator, denominator = map(int, fraction_str.split('/'))

        # Catch exception ValueError
        if denominator == 0 or numerator > denominator:
            raise ValueError

        # Calculate fuel percentage and round it to the nearest integer
        percentage = round(numerator / denominator * 100)

        # Check if tank is essentially empty or full
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return f'{percentage}%'

        # Prompt the user again if input is invalid


if __name__ == "__main__":
    fraction_str = input("Fraction: ")
    fuel_percentage = get_fuel_percentage(fraction_str)
    print(fuel_percentage)

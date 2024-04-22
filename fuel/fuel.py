def get_fuel_percentage(fraction):
    try:
        # Split the fraction into numerator and denominator
        numerator, denominator = map(int, fraction.split('/'))

        # Check for division by zero
        if denominator == 0:
            raise ZeroDivisionError

        # Check if numerator is within valid range
        if numerator > denominator or numerator < 0:
            raise ValueError

        # Calculate the percentage of fuel
        percentage = (numerator / denominator) * 100

        # Check if fuel is almost empty
        if percentage <= 1:
            return 'E'

        # Check if fuel is almost full
        elif percentage >= 99:
            return 'F'

        # Return the percentage rounded to the nearest integer
        else:
            return f"{round(percentage)}%"

    # Catch errors for invalid inputs
    except (ValueError, ZeroDivisionError):
        return None

def main():
    while True:
        # Prompt user to input a fraction
        fraction = input("Fraction: ")

        # Get the fuel percentage based on the input fraction
        percentage = get_fuel_percentage(fraction)

        # If percentage is valid, print it and exit the loop
        if percentage:
            print(percentage)
            break

        # If input is invalid, prompt user to enter a valid fraction
        else:
            print("Invalid input. Please enter a valid fraction.")

if __name__ == "__main__":
    main()

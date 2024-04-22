def get_fuel_percentage(fraction):
    try:
        # Split the fraction into numerator and denominator
        numerator, denominator = map(int, fraction.split('/'))

        # Check for division by zero
        if denominator == 0:
            raise ZeroDivisionError

        # Check if numerator is within valid range

        # Calculate the percentage of fuel

        # Check if fuel is almost empty

        # Check if fuel is almost full

        # Return the percentage rounded to the nearest integer

    # Catch errors for invalid inputs

def main():
    while True:
        # Prompt user to input a fraction

        # Get the fuel percentage based on the input fraction

        # If percentage is valid, print it and exit the loop

        # If input is invalid, prompt user to enter a valid fraction

if __name__ == "__main__":
    main()

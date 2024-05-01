def main():
    while True:
        try:
            if not fraction:
                fraction = input('Fraction: ')

            # Split the fraction into numerator and denominator
            numerator, denominator = map(int, fraction.split('/'))

            # Raise ZeroDivisionError
            if denominator == 0:
                raise ZeroDivisionError

            # Raise ValueError
            if numerator > denominator:
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
                return f'{round(percentage)}%'

        # Catch errors for invalid inputs
        except (ValueError, ZeroDivisionError):
            fraction = None
            print("Invalid input. Please enter a valid fraction.")


if __name__ == "__main__":
    print(main())

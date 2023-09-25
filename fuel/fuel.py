def main():
    while True:
        try:
            # Prompt the user for a fraction input
            fraction = input("Fraction: ")

            # Split the input into numerator and denominator, and convert them to integers
            numerator, denominator = map(int, fraction.split("/"))

            # Check for invalid input conditions
            if denominator == 0 or numerator > denominator:
                raise ValueError

            # Calculate the percentage of fuel and round it to the nearest integer
            percent = (numerator / denominator) * 100

            # Check if the tank is essentially empty (1% or less)
            if percent <= 1:
                print("E")
            # Check if the tank is essentially full (99% or more)
            elif percent >= 99:
                print("F")
            # Display the rounded percentage if it's neither empty nor full
            else:
                print(f"{round(percent)}%")

            # Exit the loop as valid input has been processed
            break
        except (ValueError, ZeroDivisionError):
            # Handle exceptions for invalid input
            print(
                "Invalid input. Please enter a valid fraction (X/Y) where X and Y are integers."
            )


if __name__ == "__main__":
    main()

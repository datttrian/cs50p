# This function is defined to get a valid fraction from the user
def get_fraction():
    while True:
        try:
            # Prompt the user for input and store it in the 'fraction' variable
            fraction = input("Fraction: ")

            # Split the input by the '/' character and convert the parts to integers
            x, y = map(int, fraction.split("/"))

            # Check if the fraction is valid (x <= y and y > 0)
            if x <= y and y > 0:
                return x, y
            else:
                print("Invalid fraction. Please try again.")

            # Handle exceptions that can occur during input or conversion
        except (ValueError, ZeroDivisionError):
            print(
                "Invalid input. Please enter a fraction in the format X/Y where X and Y are integers."
            )


# This function calculates the fuel percentage based on x and y values
def calculate_fuel_percentage(x, y):
    percentage = (x / y) * 100

    # Check the percentage and return appropriate values
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(round(percentage)) + "%"


# The main function to execute the program.
def main():
    # Get a valid fraction from the user.
    x, y = get_fraction()

    # Calculate the fuel percentage.
    result = calculate_fuel_percentage(x, y)

    # Display the result.
    print(result)


# This block ensures that the main function is executed when the script is run.
if __name__ == "__main__":
    main()

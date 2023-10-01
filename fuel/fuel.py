# This function is defined to get a valid fraction from the user
def get_fraction():
    while True:
        try:
            # Prompt the user for input and store it in the 'fraction' variable
            fraction = input("Fraction: ")

            # Split the input by the '/' character and convert the parts to integers
            x, y = map(int, fraction.split("/"))

            # Check if the fraction is valid (x <= y and y > 0)
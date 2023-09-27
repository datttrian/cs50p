# Import the inflect library to handle pluralization and formatting of names.
import inflect

# Define the main function.
def main():
    # Create an empty list to store names.
    names = []
    # Initialize the inflect engine for text manipulation.
    p = inflect.engine()

    # Start an infinite loop to input names until an empty input or EOFError is encountered.
    while True:
        try:
            # Prompt the user to input a name.
            name = input("Name: ")
            # If the input is empty, exit the loop.
            if not name:
                break
            # Append the entered name to the 'names' list.
            names.append(name)
        except EOFError:
            # Exit the loop if an End of File (EOF) error is encountered.
            break

    # Check the number of names entered and print a farewell message accordingly.
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        # Join all names except the last one with commas and add "and" before the last name.
        names_str = ", ".join(names[:-1])
        names_str += f", and {names[-1]}"
        print(f"Adieu, adieu, to {names_str}")

# Check if the script is being run as the main program.
if __name__ == "__main__":
    # Call the main function to execute the program.
    main()

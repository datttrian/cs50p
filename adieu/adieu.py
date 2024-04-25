# Import the 'inflect' module, which helps in pluralizing and singularizing English words
import inflect

def main():
    # Create an instance of the inflect engine
    p = inflect.engine()

    # Initialize an empty list to store names
    names = []

    while True:
        try:
            # Prompt the user to enter a name
            name = input("Name: ")
        except EOFError:  # Handle the end of file error (Ctrl+D in Unix-like systems)
            # Print a new line and exit the loop if the end of file is encountered
            print()
            break
        else:
            # Append the entered name to the 'names' list
            names.append(name)

    # Print a farewell message using the inflect engine to join the names with proper grammar
    print(f"Adieu, adieu, to {p.join(names)}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()

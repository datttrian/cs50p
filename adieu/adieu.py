# Import inflect to pluralize and singularize English words
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
        except EOFError:
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

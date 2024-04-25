# Import inflect to pluralize and singularize English words
import inflect

def main():
    # Create an instance of the inflect engine
    p = inflect.engine()

    # Initialize an empty list to store names
    names = []

    # Prompt the user to enter a name until the user inputs control-d
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break

        # Append the entered name to the 'names' list
        else:
            names.append(name)

    # Print a farewell message using the inflect engine to join the names with proper grammar
    print(f"Adieu, adieu, to {p.join(names)}")

if __name__ == "__main__":
    main()

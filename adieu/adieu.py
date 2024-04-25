import inflect


def main():
    # Create an empty list to store names
    names = []

    # Initialize the inflect engine for text manipulation
    p = inflect.engine()

    # Prompt the user for a item until manually stopped
    while True:
        try:

            # Prompt the user to input a name
            name = input("Name: ")

            # If the input is empty, exit the loop
            if not name:
                break

            # Append the ented name to the 'names' list
            names.append(name)

        except EOFError:
            break

    # Check the number of names entered and print a farewell message accordingly
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")

    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")

    else:
        # Join all names except the last one with commas and add "and" before the last name
        names_str = ", ".join(names[:-1])
        name_str += f", and {names[-1]}"
        print(f"Adieu, adieu, to {names_str}")


if __name__ == "__main__":
    main()

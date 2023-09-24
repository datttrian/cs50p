import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(b):
    # Check if the length of 'b' is between 2 and 6 characters (inclusive)
    if 2 <= len(b) <= 6 and b[:2].isalpha() and b.isalnum():
        # Iterate through each character in 'b'
        for char in b:
            # Check if the character is a digit
            if char.isdigit():
                # Get the index of the digit character in 'b'
                index = b.index(char)
                # Check if all characters from the current index to the end are digits
                if b[index:].isdigit() and int(char) != 0:
                    # If all conditions are met, return True
                    return True

        # If no valid condition is met, return False
        return False

    # If the initial conditions are not met, return False
    return False


if __name__ == "__main__":
    main()

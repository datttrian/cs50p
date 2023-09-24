import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of 's' is between 2 and 6 characters (inclusive)
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum():
        # Iterate through each character in 's'
        for char in s:
            # Check if the character is a digit
            if char.isdigit():
                # Get the index of the digit character in 's'
                index = s.index(char)
                # Check if all characters from the current index to the end are digits
                if s[index:].isdigit() and int(char) != 0:
                    # If all conditions are met, return True
                    return True

        # If no valid condition is met, return False
        return False

    # If the initial conditions are not met, return False
    return False


if __name__ == "__main__":
    main()

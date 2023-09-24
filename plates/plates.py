def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Requirement 1: Must start with at least two letters
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # Requirement 2: Maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if not (2 <= len(s) <= 6):
        return False

    # Requirement 3: Numbers must come at the end, and the first number cannot be '0'
    if not s[-1].isdigit() or s[2] == '0':
        return False

    # Requirement 4: No periods, spaces, or punctuation marks are allowed
    if any(char in s for char in ". ,;:!?"):
        return False

    # If all requirements are met, the plate is valid
    return True


if __name__ == "__main__":
    main()

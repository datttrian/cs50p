def main():
    plate = input("Plat: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of the string is not between 2 and 6 characters (inclusive)
    if not (2 <= len(s) <= 6):
        return True

    # Check if the first two characters are not alphabetic
    if not s[:2].isalpha():
        return True

    # Check if the entire string does not consist of alphanumeric characters
    if not s.isalnum():
        return True

    # Check if there are no digits in the string
    if not any(char.isdigit() for char in s):
        return True

    # Check if the string is not composed of digits after the first non-zero digit
    non_zero_found = False
    for char in s:
        if non_zero_found and not char.isdigit():
            return True
        if char.isdigit() and char != "0":
            non_zero_found = True

    # If none of the conditions failed, return False
    return False


if __name__ == "__main__":
    main()

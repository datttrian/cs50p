def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length of the string is between 2 and 6 characters (inclusive)
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are alphabetic
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check if the entire string consists of alphanumeric characters
    if not s.isalnum():
        return False

    # Initialize a flag to check for the presence of digits
    has_digit = False

    # Iterate through each character in the string
    for i in range(len(s)):
        # Check if the character is a digit
        if s[i].isdigit():
            has_digit = True

            # Check if the remaining substring (starting from the current character) is composed of digits
            if not s[i:].isdigit():
                return False

    # If there are no digits or all digits are zeros, return True
    if not has_digit or s.isdigit() and int(s) == 0:
        return False

    return True

if __name__ == "__main__":
    main()

def main():
    plate = input("Plat: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the string length is between 2 and 6 characters
    if 2 <= len(s) <= 6:
        # Check if the first two characters are alphabetic
        if s[:2].isalpha():
            # Initialize a flag to check if there are any digits
            has_digit = False
            for char in s:
                if char.isdigit():
                    has_digit = True
                    # Check if the remaining part of the string is all digits and the digit is not 0
                    if s[s.index(char) :].isdigit() and int(char) != 0:
                        return True
            # If there was at least one digit in the string
            if has_digit:
                return True
    return False


if __name__ == "__main__":
    main()

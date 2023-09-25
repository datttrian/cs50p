def main():
    plate = input("Plat: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of the string is between 2 and 6 characters (inclusive)
    if 2 <= len(s) <= 6:
        # Check if the first two characters are alphabetic
        if s[0:2].isalpha():
            # Check if the entire string consists of alphanumeric characters
            if s.isalnum():
                # Iterate through each character in the string
                for char in s:
                    # Check if the character is a digit
                    if char.isdigit():
                        # Get the index of the current character in the string
                        index = s.index(char)
                        # Check if the remaining substring (starting from the current character) is composed of digits
                        if s[index:].isdigit() and int(char) != 0:
                            return True
                        else:
                            return False
                # If there are no digits or all digits are zeros, return True
                return True
            # If any of the conditions fail, return False
            return False


if __name__ == "__main__":
    main()

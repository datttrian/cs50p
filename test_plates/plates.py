def main():
    plate = input("Plat: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of the string is between 2 and 6 characters (inclusive)

        # Check if the first two characters are alphabetic

            # Check if the entire string consists of alphanumeric characters

                # Iterate through each character in the string

                    # Check if the character is a digit

                        # Get the index of the current character in the string

                        # Check if the remaining substring (starting from the current character) is composed of digits




                # If there are no digits or all digits are zeros, return True

            # If any of the conditions fail, return False



if __name__ == "__main__":
    main()

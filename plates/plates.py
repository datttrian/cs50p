def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length of the string is between 2 and 6 characters
    if 2 <= len(s) <= 6:
        # Check if all characters are uppercase letters or digits
        if all(char.isalpha() or char.isdigit() for char in s):
            # Check if the first character is a letter
            if s[0].isalpha():
                # Check if numbers are only at the end
                if s[-1].isdigit() and not s[1:-1].isdigit():
                    # Check if the first number is not '0'
                    if s[-1] != '0':
                        return True
    return False

main()

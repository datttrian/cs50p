def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check if the plate starts with at least two letters
    if not re.match(r'^[A-Z]{2,}', plate):
        return False

    # Remove the letters from the plate and check for remaining characters
    remaining_chars = re.sub(r'[A-Z]', '', plate)

    # Check if the remaining characters consist of numbers only
    if not re.match(r'^[0-9]+$', remaining_chars):
        return False

    # Check if the first number is not '0'
    if remaining_chars[0] == '0':
        return False

    # Check if the total length of the plate is within the range 2-6 characters
    if len(plate) < 2 or len(plate) > 6:
        return False

    return True


if __name__ == "__main__":
    main()

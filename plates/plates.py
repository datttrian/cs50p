import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(b):
    if (
        2 <= len(b) <= 6
        and b.isalnum()
        and any(char.isdigit() and int(char) != 0 for char in b)
    ):
        return True
    return False


if __name__ == "__main__":
    main()

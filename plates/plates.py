import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(b):
    if 6 >= len(b) >= 2 and b [0:2].isalpha() and b.isalnum():
        for char in b:
            if char.isdigit():
                index = b.index(char)
                if b[index:].isdigit()and int(char) !=0:

                        return True
                else:
                    return False
        return True


if __name__ == "__main__":
    main()

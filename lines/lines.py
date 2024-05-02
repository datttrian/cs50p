import sys


def count_lines(file):
    # Outputs the number of lines of code excluding comments and blank lines
    return None


def main():
    # Expects exactly one command-line argument Python file name
    if len(sys.argv) != 2:
        sys.exit("Too few or too many arguments")
    file_name = sys.argv[1]
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")

    # Count the lines of code in the file
    try:
        with open(file_name, "r") as file:
            file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

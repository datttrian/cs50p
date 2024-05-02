import sys


def main():
    # Expect exactly one command-line argument Python file name
    if len(sys.argv) != 2:
        sys.exit("Too few or too many arguments")
    file_name = sys.argv[1]
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")

    # Count the lines of code in the file
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            non_empty_lines = [
                line.strip()
                for line in lines
                if line.strip() and not line.strip().startswith("#")
            ]
            print(len(non_empty_lines))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

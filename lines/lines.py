import sys


def count_lines(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            non_empty_lines = [
                line.strip()
                for line in lines
                if line.strip() and not line.strip().startswith("#")
            ]
            return len(non_empty_lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")

    num_lines = count_lines(file_name)
    print(
        f"Number of lines of code (excluding comments and blank lines) in {file_name}: {num_lines}"
    )


if __name__ == "__main__":
    main()

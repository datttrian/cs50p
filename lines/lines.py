import sys  # Import the sys module for handling system-related functions


def count_lines(file_name):
    # Outputs the number of lines of code excluding comments and blank lines
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
    # Expects exactly one command-line argument Python file name
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")
    file_name = sys.argv[1]
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")

    # Count the lines of code in the file
    num_lines = count_lines(file_name)
    print(
        f"Number of lines of code (excluding comments and blank lines) in {file_name}: {num_lines}"
    )


if __name__ == "__main__":
    # Call the main function when the script is executed
    main()

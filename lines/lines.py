import sys  # Import the sys module for handling system-related functions


def count_lines(file_name):
    try:
        with open(file_name, "r") as file:
            # Read all lines from the file
            lines = file.readlines()

            # Filter out empty lines and lines that start with "#" (comments)
            non_empty_lines = [
                line.strip()
                for line in lines
                if line.strip() and not line.strip().startswith("#")
            ]

            # Return the number of non-empty, non-comment lines
            return len(non_empty_lines)
    except FileNotFoundError:
        # Handle the case when the specified file does not exist
        sys.exit("File does not exist")


def main():
    if len(sys.argv) != 2:
        # Check if the correct number of command-line arguments is provided
        sys.exit("Too few or too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".py"):
        # Check if the specified file is a Python file
        sys.exit("Not a Python file")

    # Call the count_lines function to count the lines of code in the file
    num_lines = count_lines(file_name)

    # Print the result
    print(
        f"Number of lines of code (excluding comments and blank lines) in {file_name}: {num_lines}"
    )


if __name__ == "__main__":
    # Call the main function when the script is executed
    main()

import sys


def count_lines(file_name):
    # Outputs the number of lines of code excluding comments and blank lines
    with open(file_name, "r") as file:
            lines = file.readLines()
            non_empty_lines = [
                line.strip()
                for line in lines
                if line.strip() and not line.strip().startswith("#")
            ]
            return len(non_empty_lines)



def main():
    # Expects exactly one command-line argument Python file name

    # Count the lines of code in the file


if __name__ == "__main__":
    main()

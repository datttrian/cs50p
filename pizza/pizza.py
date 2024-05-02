import sys
import csv
from tabulate import tabulate


def main():
    # Expect exactly one command-line argument CSV file name
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")
    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")


    try:
        with open(file_name, newline="") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            print(data)
    except FileNotFoundError:
        sys.exit("File does not exist")




if __name__ == "__main__":
    main()

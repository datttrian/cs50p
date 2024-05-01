import sys
import csv
from tabulate import tabulate


def read_csv(file_name):
    try:
        with open(file_name, newline="") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
        return data
    except FileNotFoundError:
        sys.exit("File does not exist")


def print_pizza_table(data):
    headers = data[0]
    rows = data[1:]
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    pizza_data = read_csv(file_name)

    print_pizza_table(pizza_data)


if __name__ == "__main__":
    main()

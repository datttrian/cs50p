import csv
import sys


def main():
    # Expect exactly two command-line argument CSV file names
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Open the input CSV file
        with open(input_file, newline="") as infile:
            # Reading input CSV file as a dictionary
            reader = csv.DictReader(infile)

            # Initializing an empty list to store dictionaries
            modified_records = []

            # Modify the rows of the input CSV file
            for row in reader:
                # Split the 'name' field into first name and last name
                first_name, last_name = row["name"].split(", ")

                # Appending the dictionary containing first name, last name, and house to the list
                modified_records.append(
                    {"first": last_name, "last": first_name, "house": row["house"]}
                )

        # Open the output CSV file
        with open(output_file, "w", newline="") as outfile:
            # Create a CSV writer object with specified columns
            columns = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=columns)

            # Write the header to the output CSV file
            writer.writeheader()

            # Write the modified rows to the output CSV file
            for i in range(len(modified_records)):
                writer.writerow(
                    {
                        "first": modified_records[i]["first"],
                        "last": modified_records[i]["last"],
                        "house": modified_records[i]["house"],
                    }
                )

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()

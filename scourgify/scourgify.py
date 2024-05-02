import csv
import sys

def main():
    # Check if correct number of command-line arguments provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        listofdict = []
        # Attempt to open the input CSV file
        with open(input_file, newline='') as infile:
            # Open the output CSV file for writing
            with open(output_file, 'w', newline='') as outfile:
                reader = csv.DictReader(infile)

                # Iterate through each row of the input CSV file
                for row in reader:
                    # Split the 'name' field into first name and last name
                    first_name, last_name = row['name'].split(', ')
                    listofdict.append({"first": last_name, "last": first_name, "house": row["house"]})

                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)

                # Write the header to the output CSV file
                writer.writeheader()

                # Write the modified row to the output CSV file
                for i in range(len(listofdict)):
                    writer.writerow({"first": listofdict[i]["first"], "last": listofdict[i]["last"], "house": listofdict[i]["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()

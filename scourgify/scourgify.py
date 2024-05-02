import csv
import sys



def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input_file.csv output_file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline="") as f:
            reader = csv.DictReader(f)
            with open(output_file, "w", newline="") as output_f:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output_f, fieldnames=fieldnames)

                writer.writeheader()

                for row in reader:
                    first_name, last_name = clean_name(row["name"]).split(", ")
                    writer.writerow(
                        {"first": first_name, "last": last_name, "house": row["house"]}
                    )

        print("Conversion successful!")
    except FileNotFoundError:
        print(f"Could not read {input_file}.")
        sys.exit(1)


if __name__ == "__main__":
    main()

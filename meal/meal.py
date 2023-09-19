def main():
    # Prompt the user for input
    time_input = input("Enter the time in 24-hour format (HH:MM): ")

    # Check if the input is in the correct format
    if len(time_input) != 5 or not time_input[0:2].isdigit() or not time_input[3:].isdigit() or time_input[2] != ":":
        print("Invalid time format. Please use HH:MM.")
        return


# def convert(time):
# ...


if __name__ == "__main__":
    main()

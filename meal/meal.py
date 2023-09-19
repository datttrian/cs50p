def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")
    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)
    # Calculate the total time in hours, including minutes as fractions
    total_time = hours + (minutes / 60)
    return total_time


def main():
    # Prompt the user for input
    time_input = input("Enter the time in 24-hour format (HH:MM): ")

    # Check if the input is in the correct format
    if (
        len(time_input) != 5
        or not time_input[0:2].isdigit()
        or not time_input[3:].isdigit()
        or time_input[2] != ":"
    ):
        print("Invalid time format. Please use HH:MM.")
        return

    # Convert the input time to a float in hours
    time_in_hours = convert(time_input)

    # Check if it's mealtime and print the result
    if 7.0 <= time_in_hours <= 8.0:
        print("Breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("Dinner time")


if __name__ == "__main__":
    main()

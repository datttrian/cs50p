def main():
    # Prompt the user for a time in 24-hour format
    time_str = input("What time is it? ")

    # Convert the input time to toal hours as a float
    total_hours = convert(time_str)

    # Check if it's breakfast, lunch or dinner time
    if 7 <= total_hours < 8:
        print("breakfast time")
    elif 12 <= total_hours <= 13:
        print("lunch time")
    elif 18 <= total_hours <= 19:
        print("dinner time")
    else:
        # If it's not mealtime, don't output anything
        pass


def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")

    # Convert hours and minutes to integers and calculate the total hours
    total_hours = int(hours) + int(minutes) / 60

    return total_hours


if __name__ == "__main__":
    main()

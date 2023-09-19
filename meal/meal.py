def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")

    # Convert hours and minutes to integers and calculate the total hours
    total_hours = int(hours) + int(minutes) / 60.0

    return total_hours

def main():
    # Prompt the user for a time in 24-hour format
    time_str = input("Enter a time in 24-hour format (e.g., 7:00): ")

    # Convert the input time to total hours as a float
    try:
        total_hours = convert(time_str)

        # Check if it's breakfast time, lunch time, or dinner time
        if 7.0 <= total_hours <= 8.0:
            print("Breakfast time")
        elif 12.0 <= total_hours <= 13.0:
            print("Lunch time")
        elif 18.0 <= total_hours <= 19.0:
            print("Dinner time")
        else:
            # If it's not mealtime, don't output anything
            pass
    except ValueError:
        print("Invalid time format. Please use 24-hour format (e.g., 7:00).")

if __name__ == "__main__":
    main()

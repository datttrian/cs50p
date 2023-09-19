def convert_12_hour_time(time):
    # Split the time string into hours, minutes, and AM/PM
    parts = time.split()
    if len(parts) != 2:
        raise ValueError("Invalid time format. Please use 12-hour format (e.g., 7:00 AM or 7:00 PM).")

    time_str, am_pm = parts
    hours, minutes = time_str.split(":")

    # Convert hours and minutes to integers and calculate the total hours
    total_hours = int(hours) + int(minutes) / 60.0

    # Adjust the total hours based on AM/PM
    if am_pm.lower() == "pm":
        total_hours += 12.0

    return total_hours

def main():
    # Prompt the user for a time in 24-hour or 12-hour format
    time_str = input("Enter a time (e.g., 7:00 AM or 7:00 PM): ")

    try:
        if "am" in time_str.lower() or "pm" in time_str.lower():
            total_hours = convert_12_hour_time(time_str)
        else:
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
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

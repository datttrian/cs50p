import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regular expression to match the time formats
    pattern = r'^(\d{1,2})(?::(\d{2}))? ([AP]M) to (\d{1,2})(?::(\d{2}))? ([AP]M)$'

    # Match the input string against the pattern
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid input format")

    # Extract components from the matched groups
    start_hour, start_minute, start_ampm, end_hour, end_minute, end_ampm = match.groups()

    # Convert to 24-hour format
    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0

    # Validate hours and minutes
    if start_hour < 1 or start_hour > 12 or start_minute < 0 or start_minute > 59:
        raise ValueError("Invalid start time")
    if end_hour < 1 or end_hour > 12 or end_minute < 0 or end_minute > 59:
        raise ValueError("Invalid end time")

    # Convert AM/PM to 24-hour format
    if start_ampm == 'PM' and start_hour != 12:
        start_hour += 12
    if end_ampm == 'PM' and end_hour != 12:
        end_hour += 12

    # Handle midnight (12:00 AM)
    if start_ampm == 'AM' and start_hour == 12:
        start_hour = 0
    if end_ampm == 'AM' and end_hour == 12:
        end_hour = 0

    # Construct the 24-hour format string
    start_time = f"{start_hour:02d}:{start_minute:02d}"
    end_time = f"{end_hour:02d}:{end_minute:02d}"

    return f"{start_time} to {end_time}"


if __name__ == "__main__":
    main()

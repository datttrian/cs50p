def convert(s):
    # Regular expression to match both formats with spaces around AM/PM
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$'

    match = re.match(pattern, s)
    if match:
        # Extracting hour, minute, and AM/PM from the matched groups
        hour1, minute1, am_pm1, hour2, minute2, am_pm2 = match.groups()

        # Checking if hours and minutes are valid
        if not (0 <= int(hour1) <= 12 and 0 <= int(hour2) <= 12 and 0 <= int(minute1 or 0) < 60 and 0 <= int(minute2 or 0) < 60):
            raise ValueError("Invalid time format")

        # Convert to 24-hour format
        if am_pm1 == "PM" and hour1 != "12":
            hour1 = str(int(hour1) + 12)
        elif am_pm1 == "AM" and hour1 == "12":
            hour1 = "00"

        if am_pm2 == "PM" and hour2 != "12":
            hour2 = str(int(hour2) + 12)
        elif am_pm2 == "AM" and hour2 == "12":
            hour2 = "00"

        # Formatting the output
        return f"{hour1.zfill(2)}:{(minute1 or '00').zfill(2)} to {hour2.zfill(2)}:{(minute2 or '00').zfill(2)}"
    else:
        raise ValueError("Invalid input format")

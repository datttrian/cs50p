# fuel.py

def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if x > y:
            raise ValueError("X is greater than Y")
        if y == 0:
            raise ZeroDivisionError("Y cannot be 0")
        percentage = round((x / y) * 100)
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage out of range")
        return percentage
    except (ValueError, ZeroDivisionError):
        raise ValueError("Invalid input. Please enter a fraction in the format X/Y where X and Y are integers.")

def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(percentage) + "%"
    except TypeError:
        raise ValueError("Invalid input. Please provide a valid percentage as an integer.")

# The rest of your code remains unchanged

def main():
    x, y = get_fraction()
    result = calculate_fuel_percentage(x, y)
    print(result)

if __name__ == "__main__":
    main()

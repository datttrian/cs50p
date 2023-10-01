def main():
    fraction_str = input("Fraction: ")
    try:
        percentage = convert(fraction_str)
        result = gauge(percentage)
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print(e)

def convert(fraction_str):
    try:
        # Split the input by the '/' character and convert the parts to integers
        x, y = map(int, fraction_str.split("/"))

        # Check if X and Y are integers and Y is not 0
        if isinstance(x, int) and isinstance(y, int) and y != 0:
            # Check if X is less than or equal to Y
            if x <= y:
                percentage = (x / y) * 100
                return round(percentage)
            else:
                raise ValueError("X must be less than or equal to Y.")
        else:
            raise ValueError("X and Y must be integers, and Y must not be 0.")
    except (ValueError, ZeroDivisionError) as e:
        raise e

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError as ve:
            print(ve)
        except ZeroDivisionError as zde:
            print(zde)


def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split("/"))
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Both numerator and denominator must be integers.")
        if numerator > denominator:
            raise ValueError("Numerator cannot be greater than denominator.")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        return round((numerator / denominator) * 100)
    except ValueError:
        raise ValueError(
            "Invalid fraction format. Please enter a fraction in X/Y format where X and Y are integers."
        )


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()

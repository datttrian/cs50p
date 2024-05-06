def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)


def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split("/"))
        if numerator > denominator or denominator == 0:
            raise ValueError("Invalid fraction")
        percentage = (numerator / denominator) * 100
        return round(percentage)
    except ValueError:
        raise ValueError("Invalid fraction")
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be zero")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()

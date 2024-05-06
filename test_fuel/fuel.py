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
        if denominator == 0:
            raise ZeroDivisionError
        elif numerator > denominator:
            raise ValueError
        percentage = (numerator / denominator) * 100
        return round(percentage)
    except ValueError:
        raise ValueError("Invalid fraction")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()

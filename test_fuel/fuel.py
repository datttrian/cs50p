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


def convert(f):
    numerator, denominator = f.split("/")
    if int(denominator) == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    elif not numerator.isdigit() or not denominator.isdigit():
        raise ValueError("Numerator and denominator must be integers.")
    elif int(numerator) > int(denominator):
        raise ValueError("Numerator cannot be greater than denominator.")
    else:
        return round(int(numerator) / int(denominator) * 100)



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()

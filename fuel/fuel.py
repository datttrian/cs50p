def main():
    while True:
        fraction = input("Fraction: ")
        try:
            numerator, denominator = fraction.split("/")
            if int(denominator) == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            elif not numerator.isdigit() or not denominator.isdigit():
                raise ValueError("Numerator and denominator must be integers.")
            elif int(numerator) > int(denominator):
                raise ValueError("Numerator cannot be greater than denominator.")
            else:
                percentage = round(int(numerator) / int(denominator) * 100)
                if percentage <= 1:
                    result = "E"
                elif percentage >= 99:
                    result = "F"
                else:
                    result = str(percentage) + "%"
                print(result)
                break
        except ValueError as ve:
            print(ve)
        except ZeroDivisionError as zde:
            print(zde)


if __name__ == "__main__":
    main()

def get_fraction():
    while True:
        try:
            fraction_str = input("Fraction: ")
            x, y = fraction_str.split("/")
            x = int(x)
            y = int(y)
            if x <= y and y != 0:
                return x, y
            else:
                print("Invalid input. Please enter a valid fraction.")
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction.")


def calculate_percentage(x, y):
    percent = (x / y) * 100
    return round(percent)


def main():
    while True:
        try:
            fraction_str = input("Fraction: ")
            x, y = map(int, fraction_str.split("/"))

            if not (0 <= x <= y):
                raise ValueError(
                    "Invalid input. Numerator (X) must be between 0 and the denominator (Y)."
                )

            percent = (x / y) * 100
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{round(percent)}%")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Invalid input. {e}")


if __name__ == "__main__":
    main()

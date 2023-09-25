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
        x, y = get_fraction()
        if x / y <= 0.01:
            print("E")
        elif x / y >= 0.99:
            print("F")
        else:
            percentage = calculate_percentage(x, y)
            print(f"{percentage}%")


if __name__ == "__main__":
    main()

def main():
    while True:
        try:
            fraction_str = input("Fraction: ")
            x, y = fraction_str.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                print("Input error: Denominator cannot be zero.")
            elif not (0 <= x <= y):
                print(
                    "Input error: Numerator (X) must be between 0 and the denominator (Y)."
                )
            else:
                percent = (x / y) * 100
                if percent <= 1:
                    print("E")
                elif percent >= 99:
                    print("F")
                else:
                    print(f"{round(percent)}%")
        except ValueError:
            print(
                "Input error: Please enter a valid fraction (e.g., X/Y where X and Y are integers)."
            )


if __name__ == "__main__":
    main()

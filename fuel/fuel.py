def main():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = map(int, fraction.split("/"))

            if denominator == 0 or numerator > denominator:
                raise ValueError

            percent = (numerator / denominator) * 100
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{round(percent)}%")
            break
        except (ValueError, ZeroDivisionError):
            print(
                "Invalid input. Please enter a valid fraction (X/Y) where X and Y are integers."
            )


if __name__ == "__main__":
    main()

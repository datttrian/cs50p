def main():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = map(int, fraction.split("/"))

            
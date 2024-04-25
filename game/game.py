from random import randint


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    x = randint(1, n)

    while True:
        try:
            g = int(input("Guess: "))
            if g == x:
                print("Just right!")
                break
            elif g < x:
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()

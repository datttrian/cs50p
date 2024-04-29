from random import randint


def main():
    # Loop to prompt the user to input a positive integer
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate a random number between 1 and the level input by the user
    x = randint(1, n)

    # Loop to allow the user to guess the number
    while True:
        try:
            # Ask the user to input their guess
            g = int(input("Guess: "))

            # Check if the guess matches the random number
            if g == x:
                # Display a message if the guess is correct and ending the game
                print("Just right!")
                break

            elif g < x:
                # Display a message if the guess is smaller than the random number
                print("Too small!")

            else:
                # Display a message if the guess is larger than the random number
                print("Too large!")

        except ValueError:
            # Handle the ValueError if the input is not an integer
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()

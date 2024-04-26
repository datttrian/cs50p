from random import randint

# Defining the main function to execute the guessing game
def main():
    # Loop to prompt the user for a valid level input
    while True:
        try:
            # Asking the user to input the level
            n = int(input("Level: "))
            # Checking if the input is a positive integer
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            # Handling the ValueError if the input is invalid
            print("Invalid input. Please enter a positive integer.")

    # Generating a random number between 1 and the level input by the user
    x = randint(1, n)

    # Loop to allow the user to guess the number
    while True:
        try:
            # Asking the user to input their guess
            g = int(input("Guess: "))
            # Checking if the guess matches the random number
            if g == x:
                # Displaying a message if the guess is correct and ending the game
                print("Just right!")
                break
            elif g < x:
                # Displaying a message if the guess is smaller than the random number
                print("Too small!")
            else:
                # Displaying a message if the guess is larger than the random number
                print("Too large!")
        except ValueError:
            # Handling the ValueError if the input is not an integer
            print("Invalid input. Please enter an integer.")

# Checking if the script is being run directly
if __name__ == "__main__":
    # Calling the main function to start the game
    main()

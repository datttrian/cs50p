import random


def main():
    # Call 'get_level' to get the game level from the user
    level = get_level()

    # Generate a random target number between 1 and the chosen level
    target_number = random.randint(1, level)

    # Display a welcome message and provide the range of numbers for the guessing game
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {level}.")

    # Start a loop to repeatedly get the user's guesses until they guess correctly
    while True:
        # Call 'get_guess' to get the user's guess
        guess = get_guess()

        # Compare the user's guess with the target number and provide feedback
        if guess < target_number:
            print("Too small! Try again.")

        elif guess > target_number:
            print("Too large! Try again.")

        else:
            print(
                "Just right!"
            )  # display a success message if the guess is correct
            break


# Define a function called 'get_level' to get the user's desired game level
def get_level():
    while True:
        try:
            # Prompt the user to enter a positive integer and convert the input to an integer
            level = int(input("Enter the level (positive integer): "))

            # Check if the entered level is greater than 0
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")


# Define a function called 'get_guess' to get the user's guessed number
def get_guess():
    while True:
        try:
            # Prompt the user to enter a positive integer and convert the input to an integer
            guess = int(input("Enter your guess (positive integer): "))

            # Check if the entered guess is greater than 0
            if guess > 0:
                return guess
            else:
                print(
                    "Please enter a positive integer."
                )  # prompt for a valid positive integer if guess <= 0
        except ValueError:
            print(
                "Please enter a positive integer."
            )  # prompt for a valid positive integer if input is not an integer


if __name__ == "__main__":
    main()

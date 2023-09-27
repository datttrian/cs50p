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

        # Compare the user's guess 
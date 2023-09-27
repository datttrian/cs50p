import random

def get_level():
    while True:
        try:
            level = int(input("Enter the level (positive integer): "))
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (positive integer): "))
            if guess > 0:
                return guess
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def main():
    level = get_level()
    target_number = random.randint(1, level)

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {level}.")

    while True:
        guess = get_guess()

        if guess < target_number:
            print("Too small! Try again.")
        elif guess > target_number:
            print("Too large! Try again.")
        else:
            print("Congratulations! You guessed it right.")
            break

if __name__ == "__main__":
    main()

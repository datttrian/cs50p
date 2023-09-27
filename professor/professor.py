import random

def main():
    # Call 'get_level' to get the game level from the user and initialize the score to 0
    level = get_level()
    score = 0

    # Play 10 rounds of the game
    for _ in range(10):
        # Generate two random integers based on the selected level
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y # calculate the correct answer
        attempts = 0

        # Allow the player up to 3 attempts to answer correctly
        while attempts < 3:
            user_answer = input(f"{x} + {y} = ")

            # Check if the user's input is a valid integer
            if user_answer.isdigit():
                user_answer = int(user_answer)

                # Compare the user's answer with the correct answer
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1 # increment the score for a correct answer
                    break
                else:
                    attempts += 1 # increment the attempt count
                    if attempts == 3:
                        print(f"EEE {x} + {y} = {correct_answer}") # display the correct answer after 3 incorrect attempts
                    else:
                        print("EEE") # display an error message for non-integer input

    # Display the final score after 10 rounds
    print(f"Score: {score}")

# Define a function called 'get_level' to get the user's desired game level
def get_level():
    while True:
        try:
            # Prompt the user to enter a level and convert the input to an integer
            level = int(input("Level: "))

            # Check if the entered level is one of the valid options (1, 2, or 3)
            if level in (1,2,3):
                return level
            else:
                print("Please enter 1, 2, or 3.") # prompt for a valid level if not in the allowed range
        except ValueError:
            print("Please enter a valid level (1, 2, or 3).") # prompt for a valid level if input is not an integer

            
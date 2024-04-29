import random


def main():
    # Retrieve the difficulty level from the user
    level = get_level()

    # Initialize variables to track the number of errors and the user's score
    error = 0
    score = 0

    # Repeat the problem 10 times
    for _ in range(0, 10):

        # Prompt the user to solve the addition problem and handle input errors
        X = generate_integer(level)
        Y = generate_integer(level)
        while True:
            try:
                temp = int(input(f"{X} + {Y} = "))
                break
            except ValueError:
                print("EEE")
                error += 1
                break

        # Check if the user's answer is correct.
        if temp != X + Y:
            print("EEE")  # Print an error message if the answer is wrong.
            # Allow the user another chance to solve the problem.
            while True:
                try:
                    # Prompt again for the user's input.
                    temp = int(input(f"{X} + {Y} = "))
                except ValueError:
                    print("EEE")  # Print an error message for invalid input.
                    error += 1  # Increase the error count.
                    break  # Exit the loop on error.
                else:
                    # Check if the new answer is correct.
                    if temp == X + Y:
                        # Increase the score for the correct answer.
                        score += 1
                        break  # Exit the loop on success.
                    # Increment the error count for each wrong answer.
                    error += 1
                    print("EEE")  # Print an error message for a wrong answer.
                    # If errors reach 2, show the correct answer and reset the error count.
                    if error == 2:
                        print(f"{X} + {Y} = {X+Y}")
                        error = 0
                        break
        else:
            score += 1  # Increase the score for the correct answer.

    # After completing all iterations, print the final score.
    print("Score:", score)


def get_level():
    # Prompt the user to input level '1', '2', or '3'
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass


def generate_integer(level):
    # Generate a random integer based on the level specified
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()

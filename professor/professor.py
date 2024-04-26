import random


def main():
    # Prompt the user to choose a difficulty level
    level = get_level()

    # Get a list of problems based on the difficulty level
    problems = generate_problems(level)

    # Allow the user to attempt to solve each problem and returns the score
    score = solve_problems(problems)

    # Print the final score to the console
    print(f"Score: {score}")

def get_level():
    # Prompt the user to input level '1', '2', or '3'
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_integer(level):
    # Raise ValueError if the input provided is not one of 1, 2, or 3
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")

    # Generate a random integer based on the level specified
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def generate_problems(level):
    # Initialize an empty list to hold the problems
    problems = []

    # Get 10 random tuple (X, Y) and add them to the list
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        problems.append((X, Y))

    # Return the list of problems
    return problems

def solve_problems(problems):
    # Initialize the score to 0 to keep track of correctly solved problems
    score = 0

    # Iterate through each problem in the list of problems
    for problem in problems:

        # Calculate the correct answer for the current problem.
        X, Y = problem
        correct_answer = X + Y

        # Allow the user up to 3 attempts to solve the problem
        attempts = 0
        while attempts < 3:

            # Prompt the user to enter their answer.
            user_answer = input(f"{X} + {Y} = ")

            try:
                # Try to convert the user's answer to an integer.
                user_answer = int(user_answer)

                # Check if the user's answer is correct.
                if user_answer == correct_answer:
                    # Increment the score by 1 since the answer is correct.
                    score += 1
                    # Break out of the while loop because the problem was solved correctly.
                    break
                else:
                    # If the answer is incorrect, print "EEE" to indicate an error.
                    print("EEE")
                    # Increment the attempts counter.
                    attempts += 1
            except ValueError:
                # If the user's input is not a valid integer, print "EEE" and increment the attempts counter.
                print("EEE")
                attempts += 1
        else:
            # If the user exhausts all attempts, display the correct answer.
            print(f"The correct answer is: {correct_answer}")

    # After all problems have been attempted, return the final score.
    return score


if __name__ == "__main__":
    main()

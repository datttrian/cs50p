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

    # Generate a random integer based on the level specified.
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def generate_problems(level):
    # Initialize an empty list to hold the problems.
    problems = []

    # Loop 10 times using a for loop with a range of 10.
    for _ in range(10):
        # Call the generate_integer function with the provided level to get a random integer X.
        X = generate_integer(level)
        # Call the generate_integer function again to get another random integer Y.
        Y = generate_integer(level)
        # Add the tuple (X, Y) to the list of problems.
        problems.append((X, Y))

    # After the loop, return the list of problems containing 10 tuples of integers (X, Y).
    return problems

def solve_problems(problems):
    # Initialize the score to 0. This variable will keep track of how many problems the user solves correctly.
    score = 0

    # Iterate through each problem in the list of problems.
    for problem in problems:
        # Unpack the tuple into X and Y, which are the two numbers in the problem.
        X, Y = problem
        # Calculate the correct answer for the current problem.
        correct_answer = X + Y

        # Initialize the attempt counter to 0.
        attempts = 0

        # Allow the user up to 3 attempts to solve the problem.
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

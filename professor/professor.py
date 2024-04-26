import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print(f"Score: {score}")

def get_level():
    # Start an infinite loop. This will keep running until it is explicitly broken.
    while True:
        # Ask the user to input their level and store it in the variable 'level'.
        level = input("Level: ")

        # Check if the input level is one of '1', '2', or '3'.
        if level in ['1', '2', '3']:
            # If the level is valid, convert it to an integer and return it, breaking the loop.
            return int(level)
        else:
            # If the level is not valid, print an error message.
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_integer(level):
    # Check if the provided 'level' argument is one of the valid options: 1, 2, or 3.
    if level not in [1, 2, 3]:
        # If 'level' is not valid, raise a ValueError with a message explaining the issue.
        raise ValueError("Level must be 1, 2, or 3")

    # Generate a random integer based on the level specified.
    if level == 1:
        # If the level is 1, generate a random integer between 0 and 9, inclusive.
        return random.randint(0, 9)
    elif level == 2:
        # If the level is 2, generate a random integer between 10 and 99, inclusive.
        return random.randint(10, 99)
    elif level == 3:
        # If the level is 3, generate a random integer between 100 and 999, inclusive.
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
    score = 0
    for problem in problems:
        X, Y = problem
        correct_answer = X + Y
        attempts = 0
        while attempts < 3:
            user_answer = input(f"{X} + {Y} = ")
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        else:
            print(f"The correct answer is: {correct_answer}")
    return score

if __name__ == "__main__":
    main()

import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print(f"Score: {score}")

def get_level():
    # Start an infinite loop to continually prompt the user for input.
    while True:
        # Ask the user to enter a level and store the input in the variable 'level'.
        level = input("Level: ")

        # Check if the entered level is one of the allowed values ('1', '2', '3').
        if level in ['1', '2', '3']:
            # If the level is valid, convert the level to an integer and return it.
            return int(level)
        else:
            # If the level is not valid, inform the user and repeat the loop.
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_integer(level):
    # Check if the provided 'level' parameter is not one of the expected values (1, 2, 3).
    if level not in [1, 2, 3]:
        # If 'level' is invalid, raise a ValueError with a descriptive message.
        raise ValueError("Level must be 1, 2, or 3")

    # Check if the level is 1.
    if level == 1:
        # Return a random integer between 0 and 9 (inclusive) if the level is 1.
        return random.randint(0, 9)
    # Check if the level is 2.
    elif level == 2:
        # Return a random integer between 10 and 99 (inclusive) if the level is 2.
        return random.randint(10, 99)
    # Check if the level is 3.
    elif level == 3:
        # Return a random integer between 100 and 999 (inclusive) if the level is 3.
        return random.randint(100, 999)

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

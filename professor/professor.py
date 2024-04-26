import random

def main():
    """
    Main function to execute the program.
    """
    # Get the level of difficulty from the user
    level = get_level()

    # Generate a list of arithmetic problems based on the level
    problems = generate_problems(level)

    # Solve the generated problems and calculate the score
    score = solve_problems(problems)

    # Print the final score
    print(f"Score: {score}")

def get_level():
    """
    Prompt the user to input the level of difficulty.
    Ensure that the input is valid (1, 2, or 3).
    """
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_integer(level):
    """
    Generate a random integer based on the specified level.

    Args:
        level (int): The level of difficulty (1, 2, or 3).

    Returns:
        int: A random integer within the specified range.

    Raises:
        ValueError: If the level is not 1, 2, or 3.
    """
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def generate_problems(level):
    """
    Generate a list of arithmetic problems based on the specified level.

    Args:
        level (int): The level of difficulty (1, 2, or 3).

    Returns:
        list: A list of tuples representing arithmetic problems.
    """
    problems = []
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        problems.append((X, Y))
    return problems

def solve_problems(problems):
    """
    Solve the arithmetic problems and calculate the score.

    Args:
        problems (list): A list of tuples representing arithmetic problems.

    Returns:
        int: The total score based on the correct answers.
    """
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
                    print("Incorrect answer. Try again.")
                    attempts += 1
            except ValueError:
                print("Invalid input. Please enter an integer.")
                attempts += 1
        else:
            print(f"The correct answer is: {correct_answer}")
    return score

if __name__ == "__main__":
    main()

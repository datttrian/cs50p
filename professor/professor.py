import random

LEVELS = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
NUM_PROBLEMS = 10
MAX_ATTEMPTS = 3

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) in LEVELS:
            return int(level)
        else:
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_problems(level):
    return [(generate_integer(level), generate_integer(level)) for _ in range(NUM_PROBLEMS)]

def generate_integer(level):
    if level not in LEVELS:
        raise ValueError("Level must be 1, 2, or 3")
    return random.randint(*LEVELS[level])

def solve_problems(problems):
    score = 0
    for X, Y in problems:
        correct_answer = X + Y
        for _ in range(MAX_ATTEMPTS):
            user_answer = input(f"{X} + {Y} = ")
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
    return score

if __name__ == "__main__":
    main()

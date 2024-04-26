import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def generate_problems(level):
    problems = []
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        problems.append((X, Y))
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

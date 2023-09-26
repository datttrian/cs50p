import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        while True:
            user_answer = input(f"{x} + {y} = ")

            if user_answer.isdigit():
                user_answer = int(user_answer)

                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
            else:
                print("EEE")

    print(f"Score: {score}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid level (1, 2, or 3).")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(0, 99)
    elif level == 3:
        return random.randint(0, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()

import random


def main():
    # Retrieve the difficulty level from the user
    level = get_level()

    # Repeat a loop for 10 problems
    error = 0
    score = 0
    for _ in range(0, 10):

        # Prompt the user to answer the problem
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

        # If the answer is incorrect, print error and allow up to 2 retries
        if temp != X + Y:
            print("EEE")

            while True:
                try:
                    temp = int(input(f"{X} + {Y} = "))
                except ValueError:
                    print("EEE")
                    error += 1
                    break
                else:

                    # If the answer is correct, increase the score and exit the loop on success
                    if temp == X + Y:
                        score += 1
                        break

                    # If errors reach 2, show the correct answer and reset the error count.
                    error += 1
                    print("EEE")
                    if error == 2:
                        print(f"{X} + {Y} = {X+Y}")
                        error = 0
                        break

        # If the answer is correct, increase the score and go to the next problem
        else:
            score += 1

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

def is_great_question_answer(answer):
    # Convert the answer to lowercase and remove spaces
    answer = answer.lower().replace(" ", "")

    # Check if the answer matches "42", "forty-two", or "forty two"
    return answer == "42" or answer == "forty-two" or answer == "fortytwo"


def main():
    user_input = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )

    if is_greate_question_answer(user_input):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

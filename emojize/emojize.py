import emoji


if __name__ == "__main__":
    user_input = input("Input: ")
    emojized_output = emoji.emojize(user_input, language="alias")
    print("Output:", emojized_output)

import emoji


def main():
    user_input = input("Input: ")
    emojized_text = emoji.emojize(user_input)
    print("Output:", emojized_text)


if __name__ == "__main__":
    main()

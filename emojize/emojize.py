import emoji


def main():
    input_text = input("Input: ")
    emojized_text = emojize_text(input_text)
    print("Output:", emojized_text)


def emojize_text(input_text):
    # Use emoji.emojize to convert emoji codes and aliases to emojis
    emojized_text = emoji.emojize(input_text, use_aliases=True)
    return emojized_text


if __name__ == "__main__":
    main()

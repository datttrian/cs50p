import emoji


def emojize_text(input_text):
    # Use the emoji module to convert codes/aliases to emojis
    emojized_text = emoji.emojize(input_text, use_aliases=True)
    return emojized_text


if __name__ == "__main__":
    user_input = input("Input: ")
    emojized_output = emojize_text(user_input)
    print("Output:", emojized_output)

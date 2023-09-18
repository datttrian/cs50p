def convert(text):
    # Replace :) with 🙂
    text = text.replace(":)", "🙂")

    # Replace :( with 🙁
    text = text.replace(":(", "🙁")

    return text


def main():
    user_input = input("Enter text: ")
    converted_text = convert(user_input)
    print(converted_text)


if __name__ == "__main__":
    main()

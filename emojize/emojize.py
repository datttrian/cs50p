import emoji


def main():
    emote = input("Input: ")
    print("Output: ", end="")
    print(emoji.emojize(emote))


if __name__ == "__main__":
    main()

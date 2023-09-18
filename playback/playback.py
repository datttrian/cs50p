def main():
    # Prompt the user for input
    user_input = input("Enter text: ")

    # Replace spaces with three periods
    result = user_input.replace(" ", "...")

    # Print the modified text
    print(result)


if __name__ == "__main__":
    main()

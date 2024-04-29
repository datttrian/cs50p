def main():
    # Prompt the user for a greeting
    user_greeting = input("Enter a greeting: ")

    # Remove leading and trailling whitespace and convert the greeting to lowercase
    result = value(user_greeting)

    # Print the corresponding dollar value
    print(f"${result}")


def value(greeting):
    # Remove leading and trailing whitespace and convert the greeting to lowercase
    greeting = greeting.strip().lower()

    # Check if the greeting starts with "hello" and output the corresponding amount
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

def main():
    # Prompt the user for a greeting
    user_greeting = input("Enter a greeting: ")

    # Remove leading and trailling whitespace and convert the greeting to lowercase
    user_greeting = user_greeting.strip().lower()

    # Check if the greeting starts with "hello" and output the corresponding amount
    if user_greeting.startswith("hello"):
        print("$0")
    elif user_greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()

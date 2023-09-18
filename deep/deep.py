def main():
    # Read user inut and convert it to lowercase
    user_input = (
        input("Please enter the Answer to the Great Question: ").strip().lower()
    )

    # Check if the user input matches any of the accepted responses
    if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

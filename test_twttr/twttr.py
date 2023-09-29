def main():
    # Initialize an empty string to store the output
    output = ""

    # Prompt the user for input
    input_str = input("Input: ")

    # Iterate through each character in the input string
    for char in input_str:
        # Check if the character is a vowel (in either uppercase or lowercase)
        if char.lower() not in "aeiou":
            # If it's not a vowel, add it to the output
            output += char

    # Print the resulting string with vowels omitted
    print("Output:", output)


if __name__ == "__main__":
    main()

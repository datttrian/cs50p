def main():
    # Prompt the user for input
    input_str = input("Input: ")

    # Use the shorten function to remove vowels
    result = shorten(input_str)

    # Print the resulting string with vowels omitted
    print("Output:", result)


def shorten(input_str):
    # Initialize an empty string to store the output
    output = ""

    # Iterate through each character in the input string
    for char in input_str:
        # Check if the character is a vowel (in either uppercase or lowercase)
        if char.lower() not in "aeiou":
            # If it's not a vowel, add it to the output
            output += char

    return output


if __name__ == "__main__":
    main()

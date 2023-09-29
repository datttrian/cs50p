def main():
    # Prompt the user for input
    input_str = input("Input: ")

    # Call the shorten function to remove vowels
    output = shorten(input_str)

    # Print the resulting string with vowels omitted
    print("Output:", output)

def shorten(word):
    # Initialize an empty string to store the output
    output = ""

    # Iterate through each character in the input word
    for char in word:
        # Check if the character is a vowel (in either uppercase or lowercase)
        if char.lower() not in "aeiou":
            # If it's not a vowel, add it to the output
            output += char

    # Return the resulting string with vowels omitted
    return output

if __name__ == "__main__":
    main()

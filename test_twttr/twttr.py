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

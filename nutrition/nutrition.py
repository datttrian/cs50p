# Define a dictionary to associate fruits with their calories
fruit_calories = {
    "apple": 130,
    "banana": 110,
    "orange": 80,
    "strawberries": 50,
    "blueberries": 40,
    "grapes": 70,
    "watermelon": 80,
    "kiwi": 61,
    "mango": 150,
    "peach": 59,
    "pear": 57,
    "pineapple": 82,
    "raspberries": 64,
    "blackberries": 40,
    "avocado": 50,
    "cherries": 50,
    "apricots": 48,
    "cantaloupe": 64,
    "figs": 74,
    "pomegranate": 83,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100

}

# Prompt the user for input (fruit name)
user_input = input("Enter a fruit: ").lower()  # Convert input to lowercase for case-insensitive matching

# Check if the entered fruit exists in the dictionary
if user_input in fruit_calories:
    # If it exists, print the calories for that fruit
    print(f"Calories: {fruit_calories[user_input]}")
else:
    # If it doesn't exist, inform the user that the input is not a recognized fruit
    pass  # Do nothing for invalid input
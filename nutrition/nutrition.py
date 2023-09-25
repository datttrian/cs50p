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
}

# Prompt the user for input
item = input("Item: ").lower()  # Convert input to lowercase for case insensitivity

# Check if the input is a valid fruit in the dictionary
if item in fruit_calories:
    calories = fruit_calories[item]
    print(f"Calories: {calories}")
else:
    print("Invalid input. Please enter a valid fruit.")

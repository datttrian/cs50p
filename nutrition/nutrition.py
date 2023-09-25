def main():
    # Define a dictionary to associate fruits with their calories:
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew  melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }


# Prompt the user for input (fruit name)
user_input = input(
    "Enter a fruit: "
).lower()  # convert input to lowercase for case-insensitive matching

# Check if the entered fruit exists in the dictionary
if user_input in fruit_calories:
    # If it exists, print the calories for that fruit
    print(f"Calories: {fruit_calories[user_input]}")
else:
    # If it doesn't exist, infor the user that the input is not a recognized fruit
    pass  # do nothing for invalid input

if __name__ == "__main__":
    main()

def main():
    # Define the menu and their prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Initialize the total cost
    total_cost = 0

    try:
        while True:

            # Prompt the user to input an item
            item = input("Item: ")

            # Remove leading/trailing whitespaces
            item = item.strip()

            # Capitalize the first letter of each word
            item = item.title()

            # If the item is found in the menu
            if item in menu:

                # Add its cost to the total_cost variable
                total_cost = total_cost + menu[item]

                # Print the current total cost formatted to two decimal places
             def main():
    # Define the grocery items and their counts
    grocery_list = {}

    try:
        # Continuously prompt the user for an item until manually stopped
        while True:

            # Prompt the user to input an item
            item = input("Item: ")

            # Remove leading/trailing whitespaces
            item = item.strip()

            # Lower the words
            item = item.title()

            # If the item already exists
            if item in grocery_list:

                # Increment the count
                grocery_list[item] += 1

            # Otherwise
            else:

                # Add it to the dictionary with a count of 1
                grocery_list[item] = 1

    except EOFError:
        pass

    # Sort the dictionary by keys in a case-insensitive manner
    sorted_list = sorted(grocery_list.items(), key=lambda x: x[0].casefold())

    # Print the grocery list in the desired format
    for item, count in sorted_list:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
   print(f"Total: ${total_cost:.2f}")

            # Otherwise
            else:

                # Inform the user and prompt them to choose from the menu
                print("Invalid item. Please choose from the menu.")

    # Exit the loop when Control-D is pressed
    except EOFError:
        pass


if __name__ == "__main__":
    main()

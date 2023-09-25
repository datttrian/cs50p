def main():
    # Define the menu and their respective prices
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    # Initialize the total cost
    total_cost = 0

    # Main loop to take user input
    try:
        while True:
            item = input("Item: ").strip().title()  # Normalize user input
            if item in menu:
                total_cost += menu[item]
                print(f"Total: ${total_cost:.2f}")
            else:
                print("Invalid item. Please choose from the menu.")

    except EOFError:
        pass  # exit the loop when Control-D is pressed


if __name__ == "__main__":
    main()

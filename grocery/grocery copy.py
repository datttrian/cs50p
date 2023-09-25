def main():
    # Create an empty dictionary to store the grocery items and their counts
    grocery_list = {}

    try:
        while True:
            item = input().strip().lower()  # Read user input and convert to lowercase

            # Check if the item is already in the dictionary
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

    except EOFError:
        pass  # End of input

    # Sort the dictionary by keys in a case-insensitive manner
    sorted_list = sorted(grocery_list.items(), key=lambda x: x[0].casefold())

    # Print the grocery list in the desired format
    for item, count in sorted_list:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()

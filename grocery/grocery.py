def main():
    # Define the grocery items and their counts
    grocery_list = {}

    try:
        # Prompt the user for an item until manually stopped
        while True:

            # Prompt the user to input an item
            item = input("")

            # Remove leading/trailing whitespaces
            item = item.strip()

            # Lower the words
            item = item.lower()

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
    print()
    for item, count in sorted_list:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()

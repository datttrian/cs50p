import inflect

def bid_adieu(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        last_name = names.pop()
        names_str = ', '.join(names)
        return f"Adieu, adieu, to {names_str}, and {last_name}"

def main():
    inflect_engine = inflect.engine()
    names = []
    print("Enter names (press Ctrl+D when done):")
    try:
        while True:
            name = input("Name: ").strip()
            if name:
                names.append(name)
    except EOFError:
        pass

    if names:
        farewell_message = bid_adieu(names)
        farewell_message = inflect_engine.plural(farewell_message, len(names) != 1)
        print(farewell_message)

if __name__ == "__main__":
    main()

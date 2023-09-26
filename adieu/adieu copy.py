import inflect


def main():
    names = []
    p = inflect.engine()

    while True:
        try:
            name = input("Name: ")
            if not name:
                break
            names.append(name)
        except EOFError:
            break

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        names_str = ", ".join(names[:-1])
        names_str += f", and {names[-1]}"
        print(f"Adieu, adieu, to {names_str}")


if __name__ == "__main__":
    main()

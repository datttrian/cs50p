import inflect

def bid_adieu(names):
    engine = inflect.engine()

    num_names = len(names)

    if num_names == 1:
        return f"Adieu, adieu, to {names[0]}"

    adieu_str = ", ".join(names[:-1]) + f", and {names[-1]}"

    if num_names > 2:
        adieu_str = adieu_str.replace(",", ",", num_names - 2)

    return f"Adieu, adieu, to {adieu_str}"

def main():
    names = []
    try:
        while True:
            name = input("Name: ").strip()
            if name:
                names.append(name)
    except EOFError:
        pass

    if names:
        farewell = bid_adieu(names)
        print(farewell)

if __name__ == "__main__":
    main()

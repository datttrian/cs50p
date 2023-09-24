def main():
    amount_due = 50  # Initial amount due
    total_inserted = 0  # Total amount inserted by the user

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            total_inserted += coin
            amount_due -= coin
        else:
            print("Invalid coin. Please insert a 25, 10, or 5 cent coin.")

    if total_inserted > 50:
        change_owed = total_inserted - 50
        print(f"Change Owed: {change_owed}")
    else:
        print("Change Owed: 0")


if __name__ == "__main__":
    main()

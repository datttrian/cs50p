import sys
import requests


def main():
    # Expects the user to specify the number of Bitcoins to buy
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Queries the API for the CoinDesk Bitcoin Price Index and catch any exceptions
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_rate = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Failed to fetch Bitcoin prices")

    # Outputs the current cost to four decimal places with thousands separator
    cost = bitcoin_rate * n
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()

import sys
import requests


def main():
    # Check if there are exactly 2 command-line arguments
    if len(sys.argv) == 2:
        try:
            # Try to convert the second argument to a float
            n = float(sys.argv[1])

            # Call the btc_price function and print the result
            print(btc_price(n))

        except ValueError:
            # Handle the case where the second argument is not a number
            sys.exit("Command-line argument is not a number")

    else:
        # Handle the case where the number of arguments is not 2
        sys.exit("Missing command-line argument")


# Define a function to fetch the Bitcoin price in USD and calculate the total
def btc_price(num):
    try:
        # Send a GET request to the Coindesk API to get the current Bitcoin price
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()

        # Extract the price in USD as a floating-point number
        price = result["bpi"]["USD"]["rate_float"]

        # Calculate the total value by multiplying the price by the provided number
        total = price * num

        # Return the total formatted as a string with 4 decimal places and a "$" sign
        return f"${total:,.4f}"

    except:
        # Handle any network-related errors by returning None
        return None


if __name__ == "__main__":
    # Call the main function to start the program
    main()

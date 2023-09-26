import sys
import requests

# Check for the command-line argument
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

# Try to convert the argument to a float
try:
    bitcoins_to_buy = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# Make a request to the CoinDesk API
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error making API request: {e}")
    sys.exit(1)

# Parse the JSON response
try:
    data = response.json()
    price_usd = float(data["bpi"]["USD"]["rate_float"])
except (ValueError, KeyError):
    print("Error parsing API response")
    sys.exit(1)

# Calculate the total cost
total_cost = price_usd * bitcoins_to_buy

# Format and print the total cost with thousands separators and four decimal places
formatted_cost = f"${total_cost:,.4f}"
print(formatted_cost)

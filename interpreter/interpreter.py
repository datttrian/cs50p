def main():
    # Prompt the user for an arithmetic expression
    expression = input("Expression: ")

    # Split the input expression into its components
    operand1, operator, operand2 = expression.split(" ")

    # Convert operand1 and operand2 to integers
    operand1 = int(operand1)

    # Convert operand1 and operand2 to integers
    operand2 = int(operand2)

    # Calculate the result based on the operator
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2

    # Format and print the result to one decimal place
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()

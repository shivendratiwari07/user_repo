def add(x, y):
    # Adds two numbers and returns the result.
    return x + y

def subtract(x, y):
    # Subtracts the second number from the first and returns the result.
    return x - y

def multiply(x, y):
    # Multiplies two numbers and returns the result.
    return x * y

def divide(x, y):
    # Checks for zero division and returns the result of division if valid.
    if y == 0:
        # Avoid division by zero.
        return "Error! Division by zero."
    return x / y

def validate_input(input_str):
    """
    Validates user input to ensure it is a numeric value.
    
    Parameters:
    input_str (str): The user input to validate.
    
    Returns:
    float: The validated numeric value, or raises a ValueError if invalid.
    """
    try:
        # Convert the input to a float to ensure it's a number.
        value = float(input_str)
        return value
    except ValueError:
        # Raise an error if the input cannot be converted to a float.
        raise ValueError("Invalid input! Please enter a valid number.")

def calculator():
    """
    Runs the calculator program, allowing users to perform basic arithmetic operations.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Prompt user for operation choice.
    choice = input("Enter choice (1/2/3/4): ").strip()

    # Validate user choice.
    if choice not in {'1', '2', '3', '4'}:
        print("Invalid input! Please choose a number between 1 and 4.")
        return

    # Prompt user for two numbers and validate the inputs.
    try:
        num1 = validate_input(input("Enter first number: ").strip())
        num2 = validate_input(input("Enter second number: ").strip())
    except ValueError as e:
        print(e)
        return

    # Perform the operation based on the user's choice.
    if choice == '1':
        result = add(num1, num2)
        operation = " + "
    elif choice == '2':
        result = subtract(num1, num2)
        operation = " - "
    elif choice == '3':
        result = multiply(num1, num2)
        operation = " * "
    elif choice == '4':
        result = divide(num1, num2)
        operation = " / "

    # Display the result of the operation.
    print(f"{num1}{operation}{num2} = {result}")

if __name__ == "__main__":
    # Entry point for the calculator application.
    calculator()

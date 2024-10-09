def add(x, y):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first and returns the result.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divides the first number by the second and returns the result.
    
    Parameters:
    x (float): The numerator.
    y (float): The denominator.
    
    Returns:
    float or str: The quotient if y is not zero; otherwise, an error message.
    """
    if y == 0:
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
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")


def validate_input(input_str):
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")
    
def validate_input(input_str):
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")
def validate_input(input_str):
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")

def validate_input(input_str):
    """
    Validates user input to ensure it is a numeric value.
    
    Parameters:
    input_str (str): The user input to validate.
    
    Returns:
    float: The validated numeric value, or raises a ValueError if invalid.
    """
    try:
        value = float(input_str)
        return value
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid number.")

def calculator():
    """
    Runs the calculator program, allowing users to perform basic arithmetic operations.
    
    The user selects an operation (add, subtract, multiply, divide) and inputs two numbers.
    The function then performs the selected operation and displays the result.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in {'1', '2', '3', '4'}:
        print("Invalid input! Please choose a number between 1 and 4.")
        return

    try:
        num1 = validate_input(input("Enter first number: ").strip())
        num2 = validate_input(input("Enter second number: ").strip())
    except ValueError as e:
        print(e)
        return

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

    print(f"{num1}{operation}{num2} = {result}")

if __name__ == "__main__":
    # Entry point for the calculator application.
    calculator()





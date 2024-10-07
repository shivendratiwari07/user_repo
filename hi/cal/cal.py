def add(x, y):
    """
    Adds two numbers.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The result of x - y.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers.
    
    Parameters:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divides the first number by the second.
    
    Parameters:
    x (float): The numerator.
    y (float): The denominator.
    
    Returns:
    float or str: The quotient if y is not zero; otherwise, a warning message.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    """
    Runs a simple calculator program that allows users to perform basic arithmetic operations.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a number between 1 and 4.")

if __name__ == "__main__":
    calculator()

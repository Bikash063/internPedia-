def welcome_message():
    print("===================================")
    print("  Welcome to the Python Calculator  ")
    print("===================================\n")

def farewell_message():
    print("\n===================================")
    print("   Thank you for using the calculator!   ")
    print("===================================")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def perform_operation(operation, num1, num2):
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    return operations[operation](num1, num2)

def main():
    welcome_message()

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        operation = input("Enter your choice (1/2/3/4/5): ")

        if operation == '5':
            break

        if operation not in ['1', '2', '3', '4']:
            print("Invalid operation. Please select a valid option.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        result = perform_operation(operation, num1, num2)
        print(f"\nResult: {result}")

    farewell_message()

if __name__ == "__main__":
    main()

# Solution 1: Basic Approach Using Conditional Statements

# Get the first number from the user and convert it to a float
first_number = float(input("Enter the first number: "))

# Get the operation from the user (+, -, *, /)
operation = input("Enter operation (+, -, *, /): ")

# Get the second number from the user and convert it to a float
second_number = float(input("Enter the second number: "))

# Initialize a variable to store the result
result = None

# Perform the chosen operation using conditional statements
if operation == '+':
    # Addition
    result = first_number + second_number
elif operation == '-':
    # Subtraction
    result = first_number - second_number
elif operation == '*':
    # Multiplication
    result = first_number * second_number
elif operation == '/':
    # Division; check if the second number is not zero to avoid division by zero
    if second_number != 0:
        result = first_number / second_number
    else:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")
else:
    # Handle invalid operations
    print("Error: Invalid operation.")

# Print the result if a valid operation was performed
if result is not None:
    print(f"Result: {result}")

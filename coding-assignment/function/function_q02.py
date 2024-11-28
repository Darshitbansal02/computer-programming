# 2. Write a function that implements a basic calculator.

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operator!"

# Example usage
print(calculator(10, 5, '+'))  # Output: 15
print(calculator(10, 5, '/'))  # Output: 2.0
print(calculator(10, 0, '/'))  # Output: Error: Division by zero!

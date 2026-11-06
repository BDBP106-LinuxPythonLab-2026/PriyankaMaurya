# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None

    return a / b


# Remainder
def remainder(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None

    return a % b
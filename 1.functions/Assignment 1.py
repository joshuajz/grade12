# Author: Josh Cowan
# Date: October 8, 2020
# Filename: Assignment #1.py
# Descirption: Assignment 1: Function Based Calculator


def calc():
    # Asks for the first number (error checking)
    try:
        num1 = int(input("Number 1: "))
    except ValueError:
        print("Invalid Input -> Provide a number.")
        return

    # Asks for the second number (error checking)
    try:
        num2 = int(input("Number 2: "))
    except ValueError:
        print("Invalid Input -> Provide a number.")
        return

    # Asks for the operator
    try:
        operator = int(
            input("Operators: 1. Add | 2. Subtract |3. Multiply, 4. Divide: ")
        )
    except ValueError:
        print("Invalid Operator -> Provide a number.")
        return

    # Ensures the operator is between 1-4
    if not (1 <= operator and operator <= 4):
        print("Invalid Operator Number (ie. not between 1-4)")
        return

    # Calls the specific function and prints out the output
    if operator == 1:
        print(add(num1, num2))
    elif operator == 2:
        print(sub(num1, num2))
    elif operator == 3:
        print(mult(num1, num2))
    elif operator == 4:
        print(divide(num1, num2))

    # Asks if the user wants to play again
    again = input("Play Again? (yes/no): ")
    # If they don't, quit
    if again.lower() != "yes":
        print("Quitting")
        return
    # If they want to play again, call the function again
    else:
        calc()


# Functions for adding, subtracting, multiplying, and dividing
def add(a: int, b: int) -> str:
    return f"{a} + {b} = {a + b}"


def sub(a: int, b: int) -> str:
    return f"{a} - {b} = {a - b}"


def mult(a: int, b: int) -> str:
    return f"{a} * {b} = {a * b}"


def divide(a: int, b: int) -> str:
    return f"{a} / {b} = {a / b}"


# Call the function
calc()
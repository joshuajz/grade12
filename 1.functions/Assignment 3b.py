# Author: Josh Cowan
# Date: October 8, 2020
# Filename: Assignment #3b.py
# Descirption: Assignment 3: Hypotenuse

import math

# Hypoten^2use function a^2 + b^2 = c
def pyth(a, b):
    ab = (a * a) + (b * b)
    return math.sqrt(ab)


# Function to ask the user for an integer
def get_int(dialog):
    while True:
        try:
            response = int(input(dialog))
        except ValueError:
            print("Invalid Input")
            continue

        return response


# Asks the user for the two side lengths
def ask():
    a = get_int("Length of first side: ")
    b = get_int("Length of second side: ")

    # Prints out the hypotenuse
    print(f"Hypotenuse: {pyth(a, b)} cm\N{SUPERSCRIPT TWO}")

    # Asks the user if they want to play again
    while True:
        again = input("Play again?  y (yes) | n (no) ")

        if again.lower() not in ["y", "n"]:
            print("Invalid Input")
            continue
        break

    # IF they do, call the function again
    if again.lower() == "y":
        ask()
    else:
        print("Quitting")
        return


# Call the function
ask()

# Author: Josh Cowan
# Date: October 8, 2020
# Filename: Assignment #3a.py
# Descirption: Assignment 3: EQAO Calculator

import math


# Functions for all of the shapes
def triangle(b, h):
    return (b * h) / 2


def rect(b, h):
    return b * h


def trapezoid(a, b, h):
    return ((a + b) / 2) * h


def circle(r):
    return math.pi * (r * r)


# Function to ask the user for an integer
def get_int(dialog):
    while True:
        try:
            response = int(input(dialog))
        except ValueError:
            print("Invalid Input")
            continue

        return response


# Calculator function
def calc():
    print("What shape?")
    # Gets the shape that the user wants to calculate
    while True:
        shape_type = get_int(
            "1. Circle | 2. Rectange | 3. Trapezoid | 4. Parallelogram | 5. Triangle "
        )

        if not (1 <= shape_type and shape_type <= 5):
            print("Invalid Input")
            continue

        break

    # Iterates through every shape
    # Calls the function for the area
    # And prints out the area
    if shape_type == 1:
        radius = get_int("Radius: ")

        print(f"The area is {circle(radius)} cm\N{SUPERSCRIPT TWO}")

    elif shape_type == 2:
        length = get_int("Length: ")
        width = get_int("Width: ")

        print(f"The area is {rect(length, width)} cm\N{SUPERSCRIPT TWO}")

    elif shape_type == 3:
        base1 = get_int("Base1: ")
        base2 = get_int("Base2: ")
        height = get_int("Height: ")

        print(f"The area is {trapezoid(base1, base2, height)} cm\N{SUPERSCRIPT TWO}")

    elif shape_type == 4:
        base = get_int("Base: ")
        height = get_int("Height: ")

        print(f"The area is {rect(base, height)} cm\N{SUPERSCRIPT TWO}")

    elif shape_type == 5:
        base = get_int("Base: ")
        height = get_int("Height: ")

        print(f"The area is {triangle(base, height)} cm\N{SUPERSCRIPT TWO}")

    # Asks the user if they want to play again
    print("Play again?")
    while True:
        play_again = input("y Yes | n No ")

        if play_again.lower() not in ["y", "n"]:
            print("Invalid Input")
            return

        break

    # If they do, call the function again, otherwise quit
    if play_again == "y":
        calc()
    else:
        print("Quitting")
        return


# Call the function
calc()
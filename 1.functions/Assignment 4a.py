# Author: Josh Cowan
# Date: October 13, 2020
# Filename: Assignment #4a.py
# Descirption: Assignment 4a: Median Value


# Main function for the program
def main():
    # Prints out the median value
    med = median(get_int("Number 1: "), get_int("Number 2: "), get_int("Number 3: "))
    print(f"Median: {med}")


# Find the median value
def median(a, b, c):
    # Puts the three values into a list, sorts it, and returns  the middle value
    l = [a, b, c]
    l.sort()
    return l[1]


# Function to ask the user for an integer
def get_int(dialog):
    while True:
        try:
            response = int(input(dialog))
        except ValueError:
            print("Invalid Input")
            continue

        return response


main()
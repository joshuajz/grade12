# Author: Josh Cowan
# Date: October 5, 2020
# Filename: multiply.py
# Descirption: Assignment 5: Multipcation Table

# Stores the actual table
table = []

# The row value (top value)
row = 1

# Iterates from 1 to 12
for i in range(1, 13, 1):
    # a row value stored in a list
    l = []
    # The column value
    col = 1
    # Iterates to 12 for that specific row
    for i in range(1, 13, 1):
        # Adds the value (row * col)
        l.append(row * col)
        # Increases col for the next value
        col += 1
    # Increases row and adds the list
    row += 1
    table.append(l)

# Prints out the table

# Iterates over the rows
for row in table:
    # Iterates over each value
    for value in row:
        # Adds an amount of spaces depending on the length of the digit(s)
        if len(str(value)) == 1:
            print(value, end="   ")
        elif len(str(value)) == 2:
            print(value, end="  ")
        else:
            print(value, end=" ")
    # adds a new line after each row
    print("\n")
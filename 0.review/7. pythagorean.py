# Author: Josh Cowan
# Date: October 5, 2020
# Filename: pythagorean.py
# Descirption: Assignment 7: Pythagorean Therom Checker

# Input
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# Checks if a^2 + b^2 = c^2
if (a * a) + (b * b) == c * c:
    print("a^2 + b^2 = c^2")
    print("Therefore right angle triangle")
else:
    print("Not a right angle triangle")
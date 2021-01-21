# Author: Josh Cowan
# Date: October 8, 2020
# Filename: Assignment #3c.py
# Descirption: Assignment 3: Password Checker

import time

# Ask the user for a password
def ask_pwd():
    pwd = input(
        "Enter an 8 digit password with at least 2 numbers, 1 upper case, 1 lowercase: "
    )

    accepted = True
    # Check all of the checks for the password
    lenc = length_check(pwd)
    nc = number_check(pwd)
    lowc = lower_check(pwd)
    uc = lower_check(pwd)

    # If any of the checks are false, than the ppwd failed
    if lenc == False or nc == False or lowc == False or uc == False:
        accepted = False

    # Print out the results for each check
    print(f"Length: {'Correct' if lenc else 'Incorrect, try again'}")
    print(f"Numbers: {'Correct' if nc else 'Incorrect, try again'}")
    print(f"Lowercase: {'Correct' if lowc else 'Incorrect, try again'}")
    print(f"Uppercase: {'Correct' if uc else 'Incorrect, try again'}")

    time.sleep(0.5)

    # Determine if the password was accepted
    print("Password Accepted" if accepted else "Password Invalid")

    # If the passwod wasn't accepted, call the function again
    if accepted:
        return
    else:
        ask_pwd()


# Checks the length
def length_check(pwd):
    return False if len(pwd) < 8 else True


# Checks the amount of numbers
def number_check(pwd):
    amnt = 0
    for letter in pwd:
        if letter.isdigit():
            amnt += 1

    if amnt >= 2:
        return True
    else:
        return False
    return True if amnt >= 2 else False


# Checks the amount of lowercase letters
def lower_check(pwd):
    amnt = 0
    for letter in pwd:
        if letter.islower():
            amnt += 1

    return True if amnt >= 1 else False


# Check the amount of uppercase letters
def upper_check(pwd):
    amnt = 0
    for letter in pwd:
        if letter.isupper():
            amnt += 1

    return True if amnt >= 1 else False


# call the function
ask_pwd()
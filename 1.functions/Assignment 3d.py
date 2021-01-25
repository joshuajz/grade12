# Author: Josh Cowan
# Date: October 8, 2020
# Filename: Assignment #3c.py
# Descirption: Assignment 3: Password Checker

import string, random, time

# List of the entire alphabet (string.ascii_letters) + numbers
digits_letters = string.ascii_letters + "123456789"

# Creates a random password
def random_pwd():
    global digits_letters
    # List for the password
    pwd = []
    # Creates a password of length 4-12 (random selection)
    for i in range(random.randint(4, 12)):
        # Add something random from the string
        pwd.append(random.choice(digits_letters))

    # Return the password joined
    return "".join(pwd)


# Checks a password aganist all of the proper checks
def checks(pwd):
    print(pwd)

    # Length
    if len(pwd) < 8:
        print("Invalid. The password must be 8 charchters.")
        return False

    # Uppercase
    if sum([i.isupper() for i in pwd]) < 1:
        print("Invalid.  Need at least 1 capital letter.")
        return False

    # Lowercase
    if sum(i.islower() for i in pwd) < 1:
        print("Invalid.  Need at least 1 lowercase letter.")

    # Numbers
    if sum([i.isdigit() for i in pwd]) < 2:
        print("Invalid.  Need at least 2 numbers.")
        return False

    return True


# Creates passwords until we get a correct one
def pwd_creator():
    # Amount of attempts
    pwd_amount = 0
    while True:
        # Create a pwd + increase attempts
        pwd = random_pwd()
        pwd_amount += 1
        # Checks passwords, if they all pass
        if checks(pwd) == True:
            # Print messages + break
            print(f"The correct password is {pwd}")
            print(f"It took {pwd_amount} attempts.")
            break

        # Print a newline and wait a few seconds before the next password
        # To not clog up the console window
        print()
        time.sleep(0.2)


# Call the function
pwd_creator()
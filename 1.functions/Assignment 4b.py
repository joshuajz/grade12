# Author: Josh Cowan
# Date: October 13, 2020
# Filename: Assignment #4b.py
# Descirption: Assignment 4b: Palindromes

import time


def main():
    user_input = get_int("User Input: ")
    attempts = 0
    while True:
        reversed_input = int(str(user_input)[::-1])
        print(f"Add: {user_input} + {reversed_input} = {user_input + reversed_input}")
        user_input += reversed_input
        if check_palindrone(user_input) == True:
            attempts += 1
            print("Palindrone: TRUE!")
            print(f"Attempts: {attempts}")
            break
        else:
            attempts += 1
            print("Palindrone: FALSE")
            print(f"Attempts: {attempts}")

        time.sleep(1)


def check_palindrone(user_input):
    if str(user_input) == str(user_input)[::-1]:
        return True
    else:
        return False


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
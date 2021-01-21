# Author: Josh Cowan
# Date: October 8, 2020
# Filename: Assignment #2.py
# Descirption: Assignment 2: Games

import random


# Dice Game
def dice():
    # Loops until proper input is provided
    while True:
        # Asks for a guess, checks for a value error
        try:
            guess = int(input("What is your guess for a game of dice? 1-6 "))
        except ValueError:
            print("Invalid Input -> Provide a number.")
            continue

        # Ensures the number is between 1-6 inclusive
        if not (1 <= guess and guess <= 6):
            print("Invalid Number (1-6)")
            continue

        # We have proper input, break out
        break

    # Find a random number (1-6), and print
    ran_num = random.randint(1, 6)

    print(f"You picked {guess}, the random number was {ran_num}")


# High-Low
def high_low():
    # Loops until proper input is provided
    while True:
        # Asks for a guess, checks for a value eror
        try:
            guess = int(input("What is your guess for a game of high-low? 1-10 "))
        except ValueError:
            print("Invalid Input -> Provide a number.")
            continue

        # Ensures the guess is between 1 and 10 inclusive
        if not (1 <= guess and guess <= 10):
            print("Invalid Number (1-10)")
            continue

        # Proper Input -> Break
        break

    # Find a ranadom number (1-10), and print
    ran_num = random.randint(1, 10)

    print(f"You picked {guess}, the random number was {ran_num}")


# Rock Paper Scissors
def rps():
    # Loops until proper input is provided
    while True:
        # Asks for a guess, checks for a value error
        try:
            guess = input(
                "What is your guess for a game of rock, paper, scissors (enter rock, paper, or scissors) "
            )
        except ValueError:
            print("Invalid Input")
            continue

        # If the guess isn't 'rock', 'paper', or 'scissors'
        if guess.lower() not in ["rock", "paper", "scissors"]:
            print("Invalid Input (pick rock, paper, or scissors)")
            continue

        # Proper Input, break
        break

    # Find a random number
    # 1 -> Rock
    # 2 -> Paper
    # 3 -> Scissors
    ran_num = random.randint(1, 3)
    if ran_num == 1:
        answer = "rock"
    elif ran_num == 2:
        answer = "paper"
    elif ran_num == 3:
        answer = "scissors"

    # Print out output
    print(f"You guessed {guess} and the computer guessed {answer}")


def game():
    print("Which game would you like to play?")

    # Loop for input
    while True:
        # Checks for a value error
        try:
            game_num = int(
                input("1. Dice | 2. High-Low | 3. Rock, Paper, Scissors | 4. Quit ")
            )
        except ValueError:
            print("Invalid Input (1-4)")
            continue

        # Ensures that 1-4 was input, inclusive
        if not (1 <= game_num and game_num <= 4):
            print("Invalid Value (1-4)")
            continue

        # Proper input, break
        break

    # Finds out which game to call next, or quit
    # Provides a newline for formatting
    if game_num == 1:
        dice()
        print("\n")
    elif game_num == 2:
        high_low()
        print("\n")
    elif game_num == 3:
        rps()
        print("\n")
    elif game_num == 4:
        print("Game Over.")
        return

    # IF the user didn't quit, call the game again
    game()


# Call the function
game()
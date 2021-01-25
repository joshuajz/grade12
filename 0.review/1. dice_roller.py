# Author: Josh Cowan
# Date: October 5, 2020
# Filename: dice_roller.py
# Descirption: Assignment 1: Dice Rolling Simulator

import random, time


def main():
    # Starting cash
    cash = 100

    print("This is a dice rolling program!")
    print("Each time the dice is rolled, if the value is 4, 5, or 6 the user wins.")
    print("If 1, 2, or 3 is rolled, than the house wins.")
    print("Enter a betting amount each time, and when you wish to quit type: quit")

    # While the user has money
    while cash >= 1:
        # Ask the user for the amount they want to bet
        bet = ask_for_bet()

        # If invalid input is provided, skip
        if not bet:
            continue

        # Sleep
        time.sleep(1.5)

        # If the sentinel value is provided
        if bet == "quit":
            print("Quitting Program")
            print(f"Final Balance: {cash}")
            break

        # dice roll
        roll = random_roll()

        # Checks who won
        if roll >= 4:
            # User Wins
            cash += bet
        else:
            # House wins
            cash -= bet

        # Status message
        print(
            f"Rolled: {roll}, {'User Wins!' if roll >= 4 else 'House Wins!'} | Bet Amount: {bet} | New Balance: {cash}"
        )

    # Checks for a lack of $
    if cash <= 0:
        print("You ran out of money :(")


def random_roll():
    # Simulates a random roll
    return random.randint(1, 6)


def ask_for_bet():
    # Asks for a bet from the user
    i = input("Input a Betting Amount: ")

    # If they quit
    if i == "quit":
        return "quit"

    # Attempt to convert to an integer
    try:
        i = int(i)
    except:
        print("Invalid Input")
        return False

    # Successful conversion, return
    return i


# Run the program
main()
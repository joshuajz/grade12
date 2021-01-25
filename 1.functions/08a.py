import random
import time

random_number = 0


def displayIntro(reprint=True):
    if reprint == True:
        print(
            "Sherlock Holmes has asked you to guess the number he's thinking of between 1 in 10, in 3 guesses."
        )
        print(
            "If you succeed, he will provide you with $10, if you fail you must pay him $10."
        )
        print()
        global random_number
        random_number = random.randint(0, 10)
    else:
        print()


def chooseNumber():
    number = 100
    while not (0 <= number and number <= 10):
        print("What is your guess? ")
        number = int(input())

    return number


def checkNumber(guess):
    global random_number
    print(f"You ask if {guess} is correct? ")
    time.sleep(2)
    print(
        f"Sherlock responds that it is {'correct' if guess == random_number else 'incorrect'}."
    )
    if guess != random_number:
        time.sleep(2)
        print(
            f"Sherlock said his number is {'higher' if random_number > guess else 'lower'}."
        )
        return False
    else:
        time.sleep(0.5)
        print("You won!")
        return True


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    guess = chooseNumber()

    won = False

    if checkNumber(guess) == True:
        continue

    for i in range(2):
        displayIntro(False)

        guess = chooseNumber()

        if checkNumber(guess) == True:
            won = True
            break
    if won == False:
        print("You lose :(")
        print(f"The Number was: {random_number}.")

    print()

    print("Do you want to play again? (yes or no)")
    playAgain = input()
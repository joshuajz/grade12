import random, time


def main():
    print("1. Two Player Mode")
    print("2. Computer Mode")
    m = int(input())

    if m == 1:
        mode = "person"
    elif m == 2:
        mode = "computer"

    if mode == "computer":
        while True:
            if determine_winner(user_rps(), computer_rps()) == "exit":
                print("Exiting Program")
                break
    if mode == "person":
        while True:
            determine_user_winner(user_rps_option("A"), user_rps_option("B"))


def computer_rps():
    x = random.randint(1, 3)
    if x == 1:
        return "rock"
    if x == 2:
        return "paper"
    if x == 3:
        return "scissors"


def user_rps_option(letter):
    print("Sentinel Value: exit")
    while True:
        print(f"User: {letter}")
        i = input("Enter 'rock', 'paper', or 'scissors' (without quotes): ")
        if i == "rock" or "paper" or "scissors":
            return i
        elif i == "exit":
            return "exit"
        else:
            print("Invalid Input")


def user_rps():
    print("Sentinel Value: exit")
    while True:
        i = input("Enter 'rock', 'paper', or 'scissors' (without quotes): ")
        if i == "rock" or "paper" or "scissors":
            return i
        elif i == "exit":
            return "exit"
        else:
            print("Invalid Input")


def determine_user_winner(user_a, user_b):
    time.sleep(1.5)

    if user_a == "exit" or user_b == "exit":
        return "exit"

    print(f"User A: {user_a} | User B: {user_b}")

    if user_a == "rock":
        if user_b == "paper":
            print("User B Wins! (Paper beats Rock)\n")
            return
        if user_b == "scissors":
            print("User A Wins! (Rock beats Scissors)\n")
            return
        if user_b == "rock":
            print("Tie! (Rock and Rock)\n")
            return
    if user_a == "paper":
        if user_b == "paper":
            print("Tie! (Paper and Paper)\n")
            return
        if user_b == "scissors":
            print("User B Wins! (Scissors beats Paper)\n")
            return
        if user_b == "rock":
            print("User A Wins! (Paper beats Rock)\n")
    if user_a == "scissors":
        if user_b == "paper":
            print("User A Wins! (Scissors beats Paper)\n")
            return
        if user_b == "scissors":
            print("Tie! (Scissors and Scissors)\n")
            return
        if user_b == "rock":
            print("User B Wins! (Rock beats Scissors)\n")
            return


def determine_winner(user_rps, computer_rps):
    time.sleep(1.5)

    if user_rps == "exit":
        return "exit"

    print(f"User: {user_rps} | Computer: {computer_rps}")

    if user_rps == "rock":
        if computer_rps == "paper":
            print("Computer Wins! (Paper beats Rock)\n")
            return
        if computer_rps == "scissors":
            print("Computer Loses! (Rock beats Scissors)\n")
            return
        if computer_rps == "rock":
            print("Tie! (Rock and Rock)\n")
            return
    if user_rps == "paper":
        if computer_rps == "paper":
            print("Tie! (Paper and Paper)\n")
            return
        if computer_rps == "scissors":
            print("Computer Wins! (Scissors beats Paper)\n")
            return
        if computer_rps == "rock":
            print("User Wins! (Paper beats Rock)\n")
    if user_rps == "scissors":
        if computer_rps == "paper":
            print("User Wins! (Scissors beats Paper)\n")
            return
        if computer_rps == "scissors":
            print("Tie! (Scissors and Scissors)\n")
            return
        if computer_rps == "rock":
            print("Computer Wins! (Rock beats Scissors)\n")
            return


main()
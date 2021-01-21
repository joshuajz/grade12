import random


def pick_num():
    try:
        starting_num = int(input("Starting Number: "))
    except ValueError:
        print("Invalid Starting Number -> Provide a Number")
        return False

    try:
        ending_num = int(input("Ending Number: "))
    except ValueError:
        print("Invalid Ending Number -> Provide a Number")
        return False

    if not (starting_num < ending_num):
        print("Starting number isn't smaller than the larger number.  Invalid input.")
        return False

    if starting_num == ending_num:
        print("Starting and ending number are the same.  Invalid input.")
        return False

    random_num = random.randint(starting_num, ending_num)

    return random_num


while True:
    num = pick_num()
    if num != False:
        break

print(f"Random Number: {num}")
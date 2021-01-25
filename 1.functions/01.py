import random


def multi(num):
    try:
        num = int(num)
    except ValueError:
        print("Invalid Input provided, provide a number.")
        return False

    ran_num = random.randint(1, 10)
    print(f"Adding a random number to the input.")
    print(f"Added {ran_num} to {num} to get {num + ran_num}")
    num += ran_num

    ran_num = random.randint(1, 25)
    print("Multiplying by a random number.")
    print(f"Multiplying {num} by {ran_num} to get {num * ran_num}")
    num *= ran_num

    return num


multi(input("Enter a Number: "))
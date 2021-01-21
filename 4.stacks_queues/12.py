from collections import deque
from time import sleep


def get_input():
    amount = int(input("How many items? "))
    inputs = []
    for i in range(amount):
        inputs.append(input("Item for list: "))

    return inputs


def print_lists(l1, l2):
    print("List 1: ", l1, " | Length: ", len(l1))
    print("List 2: ", l2, " | Length: ", len(l2))
    print("")


def decrease(l1, l2):
    print("Decreasing L1, Increasing L2")
    l2.append(l1.pop())
    return l1, l2


def increase(l1, l2):
    print("Increasing L1, Decreasing L2")
    l1.append(l2.popleft())
    return l1, l2


def main():
    sleep_time = 2

    l1 = get_input()
    l2 = deque()

    print_lists(l1, l2)
    sleep(sleep_time)

    for i in range(len(l1)):
        l1, l2 = decrease(l1, l2)
        print_lists(l1, l2)
        sleep(sleep_time)
    print("_______________________________________________________")
    print("Deque: ")

    for i in range(len(l2)):
        l1, l2 = increase(l1, l2)
        print_lists(l1, l2)
        sleep(sleep_time)


main()

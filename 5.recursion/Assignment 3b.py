import random
from time import sleep

SLEEP_TIME = 1


def random_list():
    l = []
    for i in range(20):
        l.append(random.randint(1, 99))
    return l


def find_val(l, value):
    if len(l) <= 1:
        print("End of list.  FALSE.")
        sleep(SLEEP_TIME)
        return
    if l[0] + l[1] == value:
        print(l)
        print(f"{l[0]} + {l[1]} = {l[0] + l[1]}")
        print("TRUE!")
        sleep(SLEEP_TIME)
        return
    else:
        print(l)
        print(f"{l[0]} + {l[1]} = {l[0] + l[1]}")
        print("FALSE")
        l.pop(0)
        sleep(SLEEP_TIME)
        find_val(l, value)


find = int(input("Value to find: "))
find_val(random_list(), find)
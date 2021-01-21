from datetime import datetime
import random
from time import sleep
import os
from collections import deque


def main():
    jobs = get_input()
    jobs_len = len(jobs)
    for i in range(jobs_len):
        x = try_print()
        if x:
            os.system("clear")
            print_jobs(jobs)
            print("\n")
            print(f"Printed Document: {jobs[0][0]}")
            jobs.popleft()
            if i + 1 != jobs_len:
                jobs[0][1] = "printing"
        else:
            os.system("clear")
            jobs[0][1] = "error"
            print_jobs(jobs)
            print("\n")
            print(f"Error Document: {jobs[0][0]}")
            if fix_error() == False:
                print(f"Removing: {jobs[0][0]}")
                jobs.popleft()
                if i + 1 != jobs_len:
                    jobs[0][1] = "printing"
            else:
                print(f"Fixed: {jobs[0][0]}")
                jobs.popleft()
                if i + 1 != jobs_len:
                    jobs[0][1] = "printing"

        sleep(2)
        os.system("clear")
    print("Printing Complete.")


def get_input():
    name = input("Enter your name: ")
    amount = int(input("How many printjobs: "))
    jobs = deque()
    first = True
    file_extensions = (".pdf", ".doc", ".png", ".gif", ".jpg")
    for i in range(amount):
        x = [
            input("Name of file: ") + random.choice(file_extensions),
            "printing" if first else "waiting",
            name,
            datetime.now(),
        ]
        first = False
        jobs.append(x)

    return jobs


def try_print():
    x = random.randint(1, 10)
    if 1 <= x and x <= 3:
        return False
    else:
        return True


def fix_error():
    first_run = True
    while True:
        if first_run == True:
            x = int(input("Enter 1) Remove or 2) Wait: "))
            if x == 1:
                return False
            elif x == 2:
                first_run = False
                continue

        x = random.randint(1, 10)
        if 1 <= x and x <= 5:
            print("Errored Again.")
            x = int(input("Enter 1) Remove or 2) Wait: "))
            if x == 1:
                return False
            elif x == 2:
                sleep(1.5)
                continue
        else:
            return True


def print_jobs(jobs):
    print(f"{'Document Name':20}{'Status':10}{'Owner':10}{'Submitted':25}")
    for job in jobs:
        print(f"{job[0]:20}{job[1]:10}{job[2]:10}{job[3]}")


main()
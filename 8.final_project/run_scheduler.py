# Author: Josh Cowan
# Date: January 24, 2021
# Filename: run_scheduler.py
# Descirption: Setup the program for windows task scheduler.

from main import User
import os

accounts = []
for directory in os.listdir("accounts\\"):
    accounts.append(User(number=int(directory)))


for account in accounts:
    account.buy_free_game()

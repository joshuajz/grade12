from main import User
import os
from time import sleep

accounts = []
for directory in os.listdir("accounts\\"):
    accounts.append(User(number=int(directory)))

while True:
    for account in accounts:
        account.buy_free_game()

    sleep(60 * 60 * 24)
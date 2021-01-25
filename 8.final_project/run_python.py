from main import User
import os
from time import sleep


def run():
    while True:
        accounts = []
        for directory in os.listdir("accounts\\"):
            accounts.append(User(number=int(directory)))

        for account in accounts:
            account.buy_free_game()
            account.driver.close()

        print("Sleeping for 1 day.")
        sleep(60 * 60 * 24)


run()
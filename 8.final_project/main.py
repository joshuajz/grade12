# Author: Josh Cowan
# Date: January 24, 2021
# Filename: main.py
# Descirption: My Final Project!  Epic Games Free Game Claimer.

# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import ast
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, Toplevel
from shutil import rmtree

# Setup filesystem
# Creating a accounts folder
if not os.path.isdir(f"{os.getcwd()}\\accounts"):
    try:
        # Create a directory
        os.mkdir(f"{os.getcwd()}\\accounts")
    except:
        # Error message
        print(
            "Cannot create directory.  Is it on a drive that you don't have permissions for?"
        )

# User class for each "account"
class User:
    def __init__(self, number="", new_account=False, email="", password=""):
        # Number is null, figure out the largest account #, and increment
        if number == "":
            # Directory where all the accounts are stored
            account_dir = os.listdir(f"{os.getcwd()}\\accounts\\")
            # If there aren't any accounts
            if len(account_dir) == 0:
                number = 0
            else:
                # Find the last account, and increment by 1
                number = int(account_dir[-1]) + 1

        # The account number (corrosponding to the folder in accounts/)
        self.account_number = number

        # Create a webdriver to use
        self.create_driver()

        # If we're creating a new account
        if new_account:
            # Store the provided email + pwd
            self.email = email
            self.password = password

        else:
            # Pulls all of the information from the credentials.txt and cookies.txt
            self.pull_info()

            # Login
            self.login()

    def create_driver(self):
        # Start the webdriver
        try:
            # Try webdriver 88
            driver = webdriver.Chrome(
                f"{os.getcwd()}\\windows_drivers\\chromedriver88.exe"
            )
        except:
            # Try webdriver 87
            try:
                driver = webdriver.Chrome(
                    f"{os.getcwd()}\\windows_drivers\\chromedriver87.exe"
                )
            except:
                # Print out an error.  We either need a macos/linux web driver or the user needs to update chrome.
                print(
                    "Error.  You're either on an old version of chrome, or are using macos/linux.  You'll need to edit the code to change it to use the proper chromedriver."
                )

        self.driver = driver

    def pull_info(self):
        # Pull the email + password from the account folder
        with open(
            f"{os.getcwd()}\\accounts\\{self.account_number}\\credentials.txt", "r"
        ) as f:
            # Contents of the file
            contents = f.read()
            contents.split("\n")
            # Email + PWD + Username
            self.email = contents[0]
            self.password = contents[1]
            self.username = contents[2]
        # Pull the cookie
        with open(
            f"{os.getcwd()}\\accounts\\{self.account_number}\\cookies.txt", "r"
        ) as f:
            # Contents of the file
            contents = f.read()

            # Convert the textfile list of dictionaries to actual python variables
            self.cookies = ast.literal_eval(contents)

    def login(self):
        # Go to the epic games website
        self.driver.get("https://www.epicgames.com/store/en-US/")

        # Apply all the cookies
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)

        print("Added Cookies.")
        time.sleep(5)

        # Refresh the page
        self.driver.get("https://www.epicgames.com/store/en-US/")

    def store_data(self, credentials=False, cookies=False):
        # If the data hasn't already been stored
        if not os.path.isdir(f"{os.getcwd()}\\accounts\\{self.account_number}"):
            # Create the directory
            try:
                os.mkdir(f"{os.getcwd()}\\accounts\\{self.account_number}")
            except:
                print(
                    "Cannot create directory.  Is it on a drive that you don't have permissions for?"
                )

        # If we have credential storing turned on
        if credentials:
            # Store the credentials
            with open(
                f"{os.getcwd()}\\accounts\\{self.account_number}\\credentials.txt", "w"
            ) as f:
                # Write the information
                f.write(f"{self.email},{self.password},{self.username}")

        if cookies:
            # Store the cookies
            with open(
                f"{os.getcwd()}\\accounts\\{self.account_number}\\cookies.txt", "w"
            ) as f:
                # Write the cookies
                f.write(str(self.cookies))

    def buy_free_game(self):
        # Purchase the free game

        # Visit the free game part of the site
        self.driver.get("https://www.epicgames.com/store/en-US/free-games")

        # Click on the Free game
        self.driver.find_element_by_xpath(
            """//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div/div/section/div/div[1]/div/div/a/div/div/div[1]/div[2]/div/div/span"""
        ).click()

        time.sleep(5)

        # Find the "GET" button or the "OWNED" button
        for element in self.driver.find_elements_by_class_name(
            "css-70r44h-PurchaseCTA__ctaText"
        ):
            if element.text == "GET":
                # We found the game to purchase

                # Find parent element (button) + click it
                element.find_element_by_xpath("..").click()
            elif element.text == "OWNED":
                # The user already owns this free game

                print("You already have this game!")
                return True

        # Sleep to ensure the page has loaded
        time.sleep(7)

        # Find the name of the game
        for element in self.driver.find_elements_by_class_name("order-summary-title"):
            game = element.text

        print("Game Purchased: " + game)

        # Click Purchase
        self.driver.find_element_by_xpath(
            """//*[@id="purchase-app"]/div/div[4]/div[1]/div[2]/div[5]/div/div/button"""
        ).click()


#######
#######
##GUI##
#######
#######

# Global window variable
window = ""


def main():
    # Window creation
    global window
    window = tk.Tk()

    # Title
    window.title("Free Game Collector")

    # Title on the Window (ie. text saying: Epic Games: Free Game Collector)
    title_font = tkfont.Font(size=20)
    title = tk.Label(text="Epic Games: Free Game Collector", font=title_font)
    title.pack()

    # All of the accounts
    accounts = pull_accounts()

    # If there are not accounts
    if not accounts:
        print("No User Accounts.")

        # Status message on GUI
        no_accounts = tk.Label(text="There are currently no accounts. Add an account:")
        no_accounts.pack()

        # Add account button
        create_account_button = tk.Button(text="Add Account", command=create_account)
        create_account_button.pack()

    else:
        # Select an account label
        dropdown_label = tk.Label(text="Select An Account: ")
        dropdown_label.pack()

        # Dropdown for all of the accounts currently in the program
        accounts_users = [account["user"] for account in accounts]
        dropdown_value = tk.StringVar(window)
        dropdown_value.set(accounts_users[0])
        dropdown = tk.OptionMenu(window, dropdown_value, *accounts_users)
        dropdown.pack()

        # Labels for the email, password, and username
        email = tk.Label(text="")
        password = tk.Label(text="")
        username = tk.Label(text="")

        def dropdown_callback(*args):
            # Function to be called whenever a new account is selected

            for account in accounts:
                # Checking to ensure we've found the correct user
                if dropdown_value.get() == account["user"]:
                    # Pulling the account's number based on it's ID
                    account_info = pull_information(account["number"])
                    break

            # Update the email, password, and username
            email.configure(text=f"Email: {account_info['email']}")
            password.configure(text=f"Password: {'*' * len(account_info['password'])}")
            username.configure(text=f"Username: {account_info['username']}")

        # Checking for when the dropdown values change and then calling dropdown_callback
        dropdown_value.trace("w", dropdown_callback)

        # Calls it for the first time to populate the dropdown
        dropdown_callback()

        # Display the email, pwd, and username
        email.pack()
        password.pack()
        username.pack()

        def delete_account():
            # Handles account deletion

            msgbox = tk.messagebox.askquestion(
                title="Exit Application",
                message="Are you sure you wish to delete this account?",
                icon="warning",
            )

            if msgbox == "yes":
                # Delete the account

                # Find the proper directory (ie. number)
                for account in accounts:
                    if dropdown_value.get() == account["user"]:
                        correct_account = account["number"]
                        break

                # Remove the folder
                rmtree(f"{os.getcwd()}\\accounts\\{correct_account}")
                print("Removed a User.")

                # Destroy the current GUI setup and run it again w/ the new changes
                window.destroy()
                main()

        # Delete button
        delete_account_button = tk.Button(text="Delete Account", command=delete_account)
        delete_account_button.pack()

        # Create account button
        create_account_button = tk.Button(text="Add Account", command=create_account)
        create_account_button.pack()

        def start():
            # Start button
            # Will check for new free games every 24h
            window.destroy()
            while True:
                # List of all accounts
                accounts = []

                # Populating the list
                for directory in os.listdir("accounts\\"):
                    accounts.append(User(number=int(directory)))

                # Run the free game function for every program
                for account in accounts:
                    account.buy_free_game()
                    account.driver.close()

                # Sleep for 1 day
                print("Sleeping for 1 day.")
                time.sleep(60 * 60 * 24)

        # Start button
        start_button = tk.Button(text="START", command=start)
        start_button.pack()

    # Mainloop
    window.mainloop()


def create_account():
    # Adding an account to the program
    global window

    # Create a new window
    create_window = Toplevel(window)

    # Title
    create_window.title("Add Account")

    # Labels
    tk.Label(create_window, text="Add Account:", font=tkfont.Font(size=16)).grid(row=0)
    tk.Label(create_window, text="Email").grid(row=1)
    tk.Label(create_window, text="Password").grid(row=2)

    # Entries for email + password
    email_enter = tk.Entry(create_window)
    password_enter = tk.Entry(create_window, show="*")

    # Allign them in a grid
    email_enter.grid(row=1, column=1)
    password_enter.grid(row=2, column=1)

    def complete_captcha():
        # Messagebox to have the user complete the captcha
        messagebox.showinfo("Captcha", "Press okay when you've completed the captcha.")

    def account_details():
        # Pulls the account details + creates a User instance
        new_user = User(
            email=email_enter.get(), password=password_enter.get(), new_account=True
        )

        # Visit the login page
        new_user.driver.get("https://www.epicgames.com/id/login/epic")
        time.sleep(1.5)

        # Enter Credentials
        new_user.driver.find_element_by_name("email").send_keys(new_user.email)
        new_user.driver.find_element_by_name("password").send_keys(new_user.password)
        time.sleep(5)

        # Click login
        new_user.driver.find_element_by_id("sign-in").click()

        # Complete the captcha
        complete_captcha()

        # Check to see if they've been redirected to the correct page
        time.sleep(1)
        current_url = new_user.driver.current_url
        if current_url == "https://www.epicgames.com/account/personal":
            # Correct URL, goodjob
            print("\nThank you for verifying captcha.")
        else:
            # Invalid Credentials/Invalid Captcha.  Restart the process.
            messagebox.showinfo("Invalid", "Invalid Credentials or Captcha. Restart.")
            create_window.withdraw()
            new_user.driver.close()
            create_account()

        # Pulls the cookies
        new_user.cookies = new_user.driver.get_cookies()

        time.sleep(4)

        # Pulling the user's username:
        username_element = new_user.driver.find_element_by_name("displayName")
        new_user.username = username_element.get_attribute("value")

        print("Register Finished.")

        # Store the user's information
        new_user.store_data(credentials=True, cookies=True)

        # Close the GUI and restart it
        new_user.driver.close()
        create_window.withdraw()
        window.destroy()
        main()

    # Button to create a new user
    tk.Button(create_window, text="Submit", command=account_details).grid(row=3)


def pull_accounts():
    # Pulls a list of all of the accounts
    # List of dictionaries
    # user and number
    accounts = []

    # If there are no accounts, return False
    if len(os.listdir("accounts\\")) == 0:
        return False
    for directory in os.listdir(f"accounts\\"):
        with open(f"accounts\\{directory}\\credentials.txt") as f:
            contents = f.read().split(",")
            username = contents[2]
        # Add as dictionary
        accounts.append({"user": username, "number": directory})

    return accounts


def pull_information(number: int):
    # Pull the information for the number specified
    with open(f"accounts\\{number}\\credentials.txt") as f:
        account_information = f.read().split(",")

    # All of the information
    info = {}
    info["email"] = account_information[0]
    info["password"] = account_information[1]
    info["username"] = account_information[2]

    # Return
    return info

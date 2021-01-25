from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import ast
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, Toplevel

# Setup filesystem
# Creating a accounts folder
if not os.path.isdir(f"{os.getcwd()}\\accounts"):
    try:
        os.mkdir(f"{os.getcwd()}\\accounts")
    except:
        print(
            "Cannot create directory.  Is it on a drive that you don't have permissions for?"
        )


class User:
    def __init__(self, number="", new_account=False, email="", password=""):
        # Number is null, figure out the largest account #, and increment
        if number == "":
            account_dir = os.listdir(f"{os.getcwd()}\\accounts\\")
            if len(account_dir) == 0:
                number = 0
            else:
                number = int(account_dir[-1])

        # The account number (corrosponding to the folder in accounts/)
        self.account_number = number

        # Create a webdriver to use
        self.create_driver()

        if new_account:
            self.email = email
            self.password = password

            self.register_user()

            self.store_data(credentials=True, cookies=True)
        else:
            # Pulls all of the information from the credentials.txt and cookies.txt
            self.pull_info()

            # Login
            self.login()

            # TEMP: BUYING
            self.buy_free_game()

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
            contents = f.read()
            contents.split("\n")
            self.email = contents[0]
            self.password = contents[1]
        # Pull the cookie
        with open(
            f"{os.getcwd()}\\accounts\\{self.account_number}\\cookies.txt", "r"
        ) as f:
            contents = f.read()

            # Convert the textfile list of dictionaries to actual python variables
            self.cookies = ast.literal_eval(contents)

    def register_user(self):
        # Login page
        self.driver.get("https://www.epicgames.com/id/login/epic")
        time.sleep(1.5)

        # Enter Credentials
        self.driver.find_element_by_name("email").send_keys(self.email)
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(5)

        # Click login
        self.driver.find_element_by_id("sign-in").click()

        # Verify with captcha
        print("Sadly we cannot complete a captcha for you.")
        print(
            "Please complete the captcha, and then press 'enter' in the terminal window."
        )

        while True:
            inp = input()
            # If their input was ENTER
            if inp == "":
                # Check to see if they've been redirected to the correct page
                time.sleep(2)
                current_url = self.driver.current_url
                if current_url == "https://www.epicgames.com/account/personal":
                    print("\nThank you for verifying captcha.")
                    break

        self.cookies = self.driver.get_cookies()

        time.sleep(4)

        # Pulling the user's username:
        username_element = self.driver.find_element_by_name("displayName")
        self.username = username_element.get_attribute("value")

        print("Register Finished.")

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

        # Should be logged in
        # TODO: Check to ensure the login worked (ie. the user did captcha correctly.) -> Cross reference w/ username

    def store_data(self, credentials=False, cookies=False):
        if not os.path.isdir(f"{os.getcwd()}\\accounts\\{self.account_number}"):
            try:
                os.mkdir(f"{os.getcwd()}\\accounts\\{self.account_number}")
            except:
                print(
                    "Cannot create directory.  Is it on a drive that you don't have permissions for?"
                )

        if credentials:
            # Store the credentials
            with open(
                f"{os.getcwd()}\\accounts\\{self.account_number}\\credentials.txt", "w"
            ) as f:
                f.write(f"{self.email},{self.password},{self.username}")

        if cookies:
            # Store the cookies
            with open(
                f"{os.getcwd()}\\accounts\\{self.account_number}\\cookies.txt", "w"
            ) as f:
                f.write(str(self.cookies))

    def buy_free_game(self):
        self.driver.get("https://www.epicgames.com/store/en-US/free-games")

        self.driver.find_element_by_xpath(
            """//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div/div/section/div/div[1]/div/div/a/div/div/div[1]/div[2]/div/div/span"""
        ).click()

        time.sleep(5)

        for element in self.driver.find_elements_by_class_name(
            "css-70r44h-PurchaseCTA__ctaText"
        ):
            if element.text == "GET":
                # Find parent element (button) + click it
                element.find_element_by_xpath("..").click()

        time.sleep(7)

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

    accounts = pull_accounts()
    if not accounts:
        print("No User Accounts.")
        no_accounts = tk.Label(text="There are currently no accounts. Add an account:")
        no_accounts.pack()

        create_account_button = tk.Button(text="Create Account", command=create_account)
        create_account_button.pack()

    else:
        dropdown_label = tk.Label(text="Select An Account: ")
        dropdown_label.pack()

        accounts_users = [account["user"] for account in accounts]
        dropdown_value = tk.StringVar(window)
        dropdown_value.set(accounts_users[0])
        dropdown = tk.OptionMenu(window, dropdown_value, *accounts_users)
        dropdown.pack()

        email = tk.Label(text="")
        password = tk.Label(text="")
        username = tk.Label(text="")

        def dropdown_callback(*args):
            # print(accounts)
            for account in accounts:
                # print(account)
                # print(dropdown_value.get())
                if dropdown_value.get() == account["user"]:
                    account_info = pull_information(account["number"])
                    break

            email.configure(text=f"Email: {account_info['email']}")
            password.configure(text=f"Password: {'*' * len(account_info['password'])}")
            username.configure(text=f"Username: {account_info['username']}")

        dropdown_value.trace("w", dropdown_callback)

        dropdown_callback()

        email.pack()
        password.pack()
        username.pack()

        def delete_account():
            msgbox = tk.messagebox.askquestion(
                title="Exit Application",
                message="Are you sure you wish to delete this account?",
                icon="warning",
            )
            if msgbox == "yes":
                print("REMOVING ACCOUNT")
            else:
                print("BACK")

        delete_account_button = tk.Button(text="Delete Account", command=delete_account)
        delete_account_button.pack()

    # Mainloop
    window.mainloop()


def create_account():
    global window
    create_window = Toplevel(window)

    create_window.title("Add Account")

    tk.Label(create_window, text="Add Account:", font=tkfont.Font(size=16)).grid(row=0)

    tk.Label(create_window, text="Email").grid(row=1)
    tk.Label(create_window, text="Password").grid(row=2)

    email_enter = tk.Entry(create_window)
    password_enter = tk.Entry(create_window, show="*")

    email_enter.grid(row=1, column=1)
    password_enter.grid(row=2, column=1)

    def complete_captcha():
        messagebox.showinfo("Captcha", "Press okay when you've completed the captcha.")
        print("clicked")

    def account_details():
        print(email_enter.get())
        print(password_enter.get())

    tk.Button(create_window, text="Submit", command=account_details).grid(row=3)


def pull_accounts():
    accounts = []
    if len(os.listdir("accounts\\")) == 0:
        return False
    for directory in os.listdir(f"accounts\\"):
        with open(f"accounts\\{directory}\\credentials.txt") as f:
            contents = f.read().split(",")
            username = contents[2]
        accounts.append({"user": username, "number": directory})

    return accounts


def pull_information(number: int):
    with open(f"accounts\\{number}\\credentials.txt") as f:
        account_information = f.read().split(",")

    info = {}
    info["email"] = account_information[0]
    info["password"] = account_information[1]
    info["username"] = account_information[2]

    return info


# Registering a user
# x = User(new_account=True, email="cowanjzcmc1@gmail.com", password="1")
# x = User(number=0)
main()
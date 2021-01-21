from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

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
    def __init__(self, number):
        # The account number (corrosponding to the folder in accounts/)
        self.account_number = number
        self.username = ""

        # Pulls all of the information from the credentials.txt and cookies.txt
        self.pull_info()

        # Creates a chrome webdriver to use
        self.create_driver()

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
            self.cookies = contents

    def register_user(self):
        # Login page
        self.driver.get("https://www.epicgames.com/id/login/epic")
        time.sleep(1.5)

        # Enter Credentials
        self.driver.find_element_by_name("email").send_keys(self.username)
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

        # TODO: Register cookies to the file + current variable

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
        # TODO: Check to ensure the login worked (ie. the user did captcha correctly.)

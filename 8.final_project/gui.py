import tkinter as tk
import tkinter.font as tkfont
import os
from tkinter import messagebox, Toplevel
from main import User

# Setup filesystem
# Creating a accounts folder
if not os.path.isdir(f"{os.getcwd()}\\accounts"):
    try:
        os.mkdir(f"{os.getcwd()}\\accounts")
    except:
        print(
            "Cannot create directory.  Is it on a drive that you don't have permissions for?"
        )

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


main()
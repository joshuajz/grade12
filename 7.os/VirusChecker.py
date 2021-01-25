from tkinter import *
import os
from time import sleep
import subprocess
import winsound
from shutil import rmtree

app = Tk()


def checkDir():
    d = directory.get()
    createFiles()
    if not os.path.isdir(d):
        incorrectDir.pack()
        app.update()
        sleep(2)
        incorrectDir.pack_forget()
    else:
        end_files = (
            ".exe",
            ".lnk",
            ".class",
            ".jar",
            ".tmp",
            ".inf",
            ".app",
            ".cls",
            ".docx",
            ".syt",
        )
        for filename in os.listdir(d):
            with open("log.txt", "a") as f:
                f.write(f"{filename}\n")
                print(f"Checking: {filename}")
                if filename.endswith(end_files):
                    winsound.Beep(500, 500)
                    quarantine = input(
                        f"The file: {filename} is prohibited.  Would you like to quarantine the file? (y/n): "
                    ).lower()
                    if quarantine == "y":
                        # Quarantine the file
                        os.rename(
                            f"{d}/{filename}", f"{os.getcwd()}/Quarantined/{filename}"
                        )
                        sleep(1.5)
                        print("Successfully Quarantined.")
                    elif quarantine == "n":
                        # Do not quarantine the file
                        print("Didn't Quarantine.")
                elif filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
                    # Found an image file
                    print(
                        f"{filename} is an image file.  Moving it to the image folder."
                    )
                    os.rename(f"{d}/{filename}", f"{os.getcwd()}/Images/{filename}")
                    sleep(1)
                    print("Successfully Moved.")
                elif filename.endswith(".sys"):
                    # Found a system file
                    print(
                        f"{filename} is a system file.  Moving it to the system folder."
                    )
                    os.rename(f"{d}/{filename}", f"{os.getcwd()}/System/{filename}")
                    sleep(1)
                    print("Successfully Moved.")
                print()
                sleep(1)
    winsound.Beep(1000, 1000)
    print("Displaying Log File: ")
    subprocess.call(["notepad", f"{os.getcwd()}\log.txt"])
    sleep(5)
    print("\nDisplaying Qurantined Folder: ")
    for filename in os.listdir(f"{os.getcwd()}\Quarantined"):
        print(f"{filename}")
        sleep(0.1)
    sleep(0.5)
    delete = input("\nWould you like to delete the quarantine folder? (y/n): ").lower()
    # Save log file for quarantined
    with open("quarantined.txt", "a") as f:
        f.write("Quarantined Files:\n\n")
        for filename in os.listdir(f"{os.getcwd()}\Quarantined"):
            f.write(f"{filename}\n")

    if delete == "y":
        # Delete the folder
        rmtree(f"{os.getcwd()}\Quarantined")
        print("Quarantine Folder Removed Successfully.")

    subprocess.call(["notepad", f"{os.getcwd()}\quarantined.txt"])

    print("Quarantine Log Displayed.")
    print("\nProcess is finished.")


def createFiles():
    d = os.getcwd()
    # Create log file
    f = open("log.txt", "a")
    f.truncate(0)
    f.write("Log:\n\n")
    f.close()
    os.mkdir(f"{d}\Quarantined")
    os.mkdir(f"{d}\Images")
    os.mkdir(f"{d}\System")


def show():
    p = password.get()  # get password from entry
    if p == "password":
        print("yes")

        dirEntry.pack()

        submitDir.pack()
        passEntry.pack_forget()
        submit.pack_forget()

    else:
        print("no")


password = StringVar()  # Password variable
directory = StringVar()  # Directory Varialbe

dirEntry = Entry(app, textvariable=directory)
passEntry = Entry(app, textvariable=password, show="*")
submit = Button(app, text="Show Console", command=show)
submitDir = Button(app, text="Submit Directory", command=checkDir)
incorrectDir = Label(app, text="Incorrect Directory.")


passEntry.pack()

submit.pack()

app.mainloop()

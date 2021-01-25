# Author: Josh Cowan
# Date: October 5, 2020
# Filename: database.py
# Descirption: Assignment 4: Database


def main():
    print("The database is currently emptey.  Add a person to the database first.")

    # List of all the people in the database
    list_people = []

    # Adds the very first person to the list
    add_person(list_people)

    # Runs continuously
    while True:
        # Lists all the people
        print(f"List of people in the database: {[i['name'] for i in list_people]}")

        # Menu Options
        print("1. Add another user to the database.")
        print("2. Lookup a person in the database.")
        print("3. Quit")
        num = int(input())

        if num == 1:
            # Adds another user to the database
            add_person(list_people)
        elif num == 2:
            # Looks up a person
            name_look = input("Person's Name: ")
            # Iterates through every name
            for name in list_people:
                # If we found the value
                if name["name"] == name_look:
                    # Print the information
                    print(
                        f"Name: {name['name']} | Phone Number: {name['phone_number']} | Address: {name['address']} | Email: {name['email']}"
                    )
                    continue
            print("Invalid Name")

        elif num == 3:
            print("Quitting.")
            break
        else:
            print("Invalid Name.")


def create_person(name, number, address, email, l):
    l.append({"name": name, "phone_number": number, "address": address, "email": email})


def add_person(l):
    print("Adding a new user to the database: ")
    name = input("Enter the name: ")
    number = input("Enter the phone number: ")
    address = input("Enter the address: ")
    email = input("Enter the email: ")
    create_person(name, number, address, email, l)


main()
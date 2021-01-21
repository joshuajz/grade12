# Author: Josh Cowan
# Date: October 5, 2020
# Filename: text_file.py
# Descirption: Assignment 2: Text File - Counts words in a text file


def main():
    # Opens the file
    with open("paragraph.txt", "r") as f:
        # Create a dictionary
        d = {}

        # For every line in the file (split @ spaces)
        for w in f.readlines()[0].split(" "):
            # Remove unwanted charchters (ie. \n , .)
            w = w.replace("\n", "")
            w = w.replace(".", "")
            w = w.replace(",", "")

            # If the value is already in the dictionary, increment
            if w in d:
                d[w] += 1
            else:
                # Create the value in the program
                d[w] = 1

        create_file(d)


def create_file(dict):
    # Takes a dictionary as input and writes it to a file

    # Opens file
    with open("output.txt", "a") as f:
        # Clears file if it's been run before
        f.truncate(0)
        # For every value in the dictionary
        for key, value in enumerate(dict):
            # Write to the file
            f.write(f"{value} | {dict[value]}\n")


# Run the program
main()
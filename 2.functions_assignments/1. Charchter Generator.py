# Author: Josh Cowan
# Date: October 15, 2020
# Filename: 1. Charchter Generator.py
# Descirption: Functions Project 1 - Charchter Generator
import random, os


# The logo
def print_logo():
    return """   _____ _                          _               _____                           _             
  / ____| |                        | |             / ____|                         | |            
 | |    | |__   __ _ _ __ __ _  ___| |_ ___ _ __  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |    | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |____| | | | (_| | | | (_| | (__| ||  __/ |    | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|_| |_|\__,_|_|  \__,_|\___|\__\___|_|     \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                  
                                                                                                  """


# ALl of the charchter's different ASCII Art
def char_logo(char):
    if char == "Fighter":
        return """               /\\_[]_/\\
              |] _||_ [|
       ___     \\/ || \\/
      /___\\       ||
     (|0 0|)      ||
   __/{\\U/}\\_ ___/vvv
  / \\  {~}   / _|_P|
  | /\\  ~   /_/   []
  |_| (____)        
  \\_]/______\\        
     _\\_||_/_           
    (_,_||_,_)"""
    if char == "Mage":
        return """                       ,---.
                       /    |
                      /     |
                     /      |
                    /       |
               ___,'        |
             <  -'          :
              `-.__..--'``-,_\\_
                 |o/ ` :,.)_`>
                 :/ `     ||/)
                 (_.).__,-` |\\
                 /( `.``   `| :
                 \\'`-.)  `  ; ;
                 | `       /-<
                 |     `  /   `.
 ,-_-..____     /|  `    :__..-'\\
/,'-.__\\\\  ``-./ :`      ;       \\
`\\ `\\  `\\\\  \\ :  (   `  /  ,   `. \\
  \\` \\   \\\\   |  | `   :  :     .\\ \\
   \\ `\\_  ))  :  ;     |  |      ): :
  (`-.-'\\ ||  |\\ \\   ` ;  ;       | |
   \\-_   `;;._   ( `  /  /_       | |
    `-.-.// ,'`-._\\__/_,'         ; |
       \\:: :     /     `     ,   /  |
        || |    (        ,' /   /   |
        ||                ,'   /    |"""

    if char == "Thief":
        return """
                       __.------.                          
                      (__  ___   )                         
                        .)e  )\\ /                          
                       /_.------                           
                       _/_    _/                           
                   __.'  / '   `-.__                       
                  / <.--'           `\\                     
                 /   \\   \\c           |                    
                /    /    )  GoT  x    \\                   
                |   /\\    |c     / \\.-  \\                  
                \\__/  )  /(     (   \\   <>'\\               
                     / _/ _\\-    `-. \\/_|_ /<>             
                    / /--/,-\\     _ \\     <>.`.            
                    \\/`--\\_._) - /   `-/\\    `.\\           
                     /        `.     /   )     `\\          
                     \\      \\   \\___/----'                 
                     |      /    `(                        
 ___________         \\    ./\\_   _ \\                       
   ______________    /     |  )    '|                      
 __________________ |     /   \\     \\     ___________a:f   
                   /     |     |____.)                     
                  /      \\  a88a\\___/88888a.               
                 \\_      :)8888888888888888888a.           
                /` `-----'  `Y88888888888888888            
                \\____|         `88888888888P' """
    if char == "Cleric":
        return """       .....           .....
   ,ad8PPPP88b,     ,d88PPPP8ba,
  d8P"      "Y8b, ,d8P"      "Y8b
 dP'           "8a8"           `Yd
 8(              "              )8
 I8                             8I
  Yb,                         ,dP
   "8a,                     ,a8"
     "8a,                 ,a8"
       "Yba             adP"   
         `Y8a         a8P'
           `88,     ,88'
             "8b   d8"
              "8b d8"
               `888'
                 "
"""
    if char == "Assassin":
        return """            |
////////////|---------------------------------,
`^^^^^^^^^^^|--------------------------------"
            |"""


# Creates a charchter
def create():
    # Clears the console
    os.system("clear")
    print(print_logo())
    # Asks for a name, clears console, and returns name
    name = get_string("Name of Charchter: ")
    os.system("clear")

    return name


# Function to get a string from the user
def get_string(dialog: str):
    while True:
        try:
            string = input(dialog)
        except ValueError:
            continue

        return string


# Builds a charchter
def build_character(name: str):
    # Assigns the random points to the skills
    def random_points():
        # Range: 4-9

        # Everything must have at least 4 points, so we might aswell start at 4 points and subtract 24
        total_points = 37 - (4 * 6)
        # Dict with all the skills
        skills = {
            "Strength": 4,
            "Intelligence": 4,
            "Constitution": 4,
            "Dexterity": 4,
            "Piety": 4,
            "Luck": 4,
        }
        # Administor points until we have none left to give
        while total_points > 0:
            # Pick a random skill
            element = random.choice(list(skills))
            # Check to see if the skill has less than 9 points
            if skills[element] < 9:
                # Increase the amount of points and decrement the amount to administor
                skills[element] += 1
                total_points -= 1
        # Return the skills
        return skills

    # ALlows the user to assign the remaining points
    def administor_points(skills: dict):
        # Loops until the 3 are assigned
        admin_points = 3
        while admin_points > 0:
            # Prints the current information (ie. logo, name, and skills)
            print(print_logo())
            print("\u0332".join(name + " "))
            print_skills(skills)
            print()

            # How many points are left
            print(
                f"You have {admin_points} more {'points' if admin_points > 1 else 'point'} to distribute to any attribute."
            )

            # Determines the current class(es)
            determine_class(skills, output=True)

            # Asks the user for a skill, loops until proper input is provided
            while True:
                increase = get_string(
                    "\nWhich attribute would you like to upgrade?  (Enter the name.  ie. Strength) "
                )
                if increase.lower() in [
                    "strength",
                    "dexterity",
                    "consitution",
                    "intelligence",
                    "piety",
                    "luck",
                ]:
                    break
            # INcrements that skill, decreaes amount of points to provide, and clears the screen
            skills[increase.capitalize()] += 1
            admin_points -= 1
            os.system("clear")
        # Returns the final skills
        return skills

    # Runs the two functions and returns the final skills
    skills = random_points()
    skills = administor_points(skills)
    return skills


# Prints out all of the skills, nicely formatted
def print_skills(skills: dict):
    for skill in skills:
        print(f"{str(skill):13s}: {str(skills[skill])}")


# Determine's the user's class(es)
def determine_class(skills: dict, output: bool = False):
    # The Classes
    classes = []

    # Requirements
    if skills["Strength"] >= 7 and skills["Dexterity"] >= 7:
        classes.append("Fighter")
    if skills["Intelligence"] >= 8 and skills["Constitution"] >= 9:
        classes.append("Mage")
    if skills["Dexterity"] >= 7 and skills["Luck"] >= 9:
        classes.append("Thief")
    if skills["Piety"] >= 9 and skills["Intelligence"] >= 6:
        classes.append("Cleric")
    if skills["Luck"] >= 5 and skills["Strength"] >= 8 and skills["Dexterity"] >= 7:
        classes.append("Assassin")
    if len(classes) == 0:
        classes.append("No Class")

    # Prints out the classes if output is turned on
    if output:
        if len(classes) == 1:
            print(f"\nYour character is currently a {classes[0]}.")
        if len(classes) == 2:
            print(f"\nYour character is currently a {classes[0]} and {classes[1]}.")
        if len(classes) >= 3:
            print(f"\nYour character is currently a ")
            for c in classes:
                print(f"{c}, ", end="")
            print(".")

    # Returns the list of classes
    return classes


# Writes the charchter sheet to a text file w/ the name of the charchter
def write_sheet(name: str, skills: dict):
    with open(f"{name}.txt", "a") as f:
        # Clears the file
        f.truncate(0)

        # Writes the logo, name, skills, and classes
        f.write(f"{print_logo()}\n")
        f.write(f"{name}\n")
        for skill in skills:
            f.write(f"{str(skill):13s}: {str(skills[skill])}\n")

        classes = determine_class(skills, output=False)
        if len(classes) == 1:
            f.write(f"\nYour character is currently a {classes[0]}.\n")
        if len(classes) == 2:
            f.write(f"\nYour character is currently a {classes[0]} and {classes[1]}.\n")
        if len(classes) >= 3:
            f.write(f"\nYour character is currently a ")
            for c in classes:
                f.write(f"{c},")
            f.write(".\n")

        # Writes the ASCII art for the classes (ie. each class has an art for the bottm of the page)
        for c in determine_class(skills):
            if c != "No Class":
                f.write(char_logo(c))
                f.write("\n")
    # Provides a successful status message
    print(f"Successfully Wrote to file: {name}.txt.")


# Runs the main program
def main():
    # Finds the name
    name = create()
    # Generates + Asks for the skills
    skills = build_character(name)
    # Prints the logo, name, skills, and classes
    print(print_logo())
    print("\u0332".join(name + " "))
    print_skills(skills)
    determine_class(skills, output=True)

    # Asks the user if they like their sheet
    while True:
        repeat = get_string(
            '\nAre you happy with your sheet?  If you are happy with your sheet enter "yes" otherwise enter "no". '
        )
        # IF they aren't happy, clear the terminal and rerun
        if repeat.lower() == "no":
            # Clear the termianl window, and rerun the program
            os.system("clear")
            main()
            break
        # IF they are happy, print out the file and exit
        elif repeat.lower() == "yes":
            write_sheet(name, skills)
            break


main()
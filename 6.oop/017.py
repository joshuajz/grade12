class enemy:
    def __init__(self):
        self.colour = input("Colour: ")
        self.hp = int(input("HP: "))
        self.ac = int(input("Armor Class: "))
        self.weapon = input("Weapon: ")

    def print_attrib(self, attrib):
        if attrib == "Colour":
            print(self.colour)
        elif attrib == "HP":
            print(self.hp)
        elif attrib == "Armor Class":
            print(self.ac)
        elif attrib == "Weapon":
            print(self.weapon)
        else:
            return False


x = enemy()
while True:
    if (
        x.print_attrib(input("Attribute to print (Colour, HP, Armor Class, Weapon): "))
        == False
    ):
        break
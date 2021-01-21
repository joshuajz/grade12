class Badguy:
    def __init__(self, name):

        self.hp = 4
        self.name = name

    def attack(self):
        print(f"{self.name}:hit")
        self.hp -= 1

    def still_alive(self):
        if self.hp <= 0:
            print(str(self.name) + " destroyed")
        else:
            print(str(self.name) + ":" + str(self.hp) + " hp left")


enemy1 = Badguy("enemy1")
enemy2 = Badguy("enemy2")

enemy1.attack()
enemy1.attack()
enemy1.still_alive()
enemy2.still_alive()
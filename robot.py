
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Ultralight Beam", 50)

    def attack(self, dinosaur):
      print(f'{dinosaur} has been attacked')

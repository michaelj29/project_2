
from robot_vs_dinosaur.weapons import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon()

    def attack(self, dinosaur):
        pass
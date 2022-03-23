from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinos = []

    def create_herd(self):
      self.dinos.append(Dinosaur("Little Foot", 50))
      self.dinos.append(Dinosaur("T-rex", 100))
      self.dinos.append(Dinosaur("Geico Lizard", 15))

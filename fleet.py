from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self): 
      self.robots.append(Robot("I-Robot"))
      self.robots.append(Robot("The terminator"))
      self.robots.append(Robot("Alexa"))
 
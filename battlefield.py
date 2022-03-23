import re
from fleet import Fleet
from herd import Herd
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


# ! 1 Display welcome message
# ! 2 Create the two teams that will face each other
# ! 3 Show the current stats of both teams in the battle 
# ! 4 Decide which Dinosaur you want to use to attack the Robots

# ! 6 Decide which Robot you want to attack 
# ! 7 Attack the Robot
# ! 8 Print the current Robots list displaying their name and health
# ! 9 Decide which Robot you want to use to attack the Dinosuars
# ! 10 Decide the weapon (theres ony one weapon) you want to use to attack the Dinosaurs
# ! 11 Decide which Dinosaur you want to attack
# ! 12 Attack the robot
# ! 13 Print the current Dinosaurs list displaying their name, health, and attack_power
# ! 14 Repeat steps 4 - 13 until health from either team is depleted
# ! 15 Return the Winner ! 

    def run_game(self):
        self.display_welcome()
        self.battle()
 
    
    # Step #1
    def display_welcome(self):
        print("------------------------------")
        print("Welcome to Robos vs. Dinos !!")
        print("--------------Team Robos----------------")
        print("                  VS                    ")
        print("--------------Team Dinos----------------")

    def battle(self):
        # Step #2 
        self.fleet.create_fleet()
        self.herd.create_herd()
        team_robos = self.fleet
        team_dinos = self.herd


        def show_dino_opponent_option(self):
    # Show the dino stats of the current battle 
    # prints the current health and attack power of the dinosaur
          print("------------------------------")
          print(f'{team_robos.robots[0].name}, Health: {team_robos.robots[0].health}, Attack Power: {team_robos.robots[0].weapon.attack_power}')
          print(f'{team_robos.robots[1].name}, Health: {team_robos.robots[1].health}, Attack Power: {team_robos.robots[1].weapon.attack_power}')
          print(f'{team_robos.robots[2].name}, Health: {team_robos.robots[2].health}, Attack Power: {team_robos.robots[2].weapon.attack_power}')
          print("------------------------------")
    
        def show_robo_opponent_option(self):
    # Show the robot stats of the current battle
    # prints the current health and of the dinosaur
          print("------------------------------")
          print(f'{team_dinos.dinos[0].name}, Health: {team_dinos.dinos[0].health}, Attack Power: {team_dinos.dinos[0].attack_power}')
          print(f'{team_dinos.dinos[1].name}, Health: {team_dinos.dinos[1].health}, Attack Power: {team_dinos.dinos[1].attack_power}')
          print(f'{team_dinos.dinos[2].name}, Health: {team_dinos.dinos[2].health}, Attack Power: {team_dinos.dinos[2].attack_power}')
          print("------------------------------")
          
        def dino_turn(self, dinosaur):
        # Which Dinosaur deals the damage to the current robot
        
          if team_dinos.dinos[0].health + team_dinos.dinos[1].health + team_dinos.dinos[2].health <= 0:
              return 0
          elif team_dinos.dinos[dinosaur].attack_power < 30: 
              team_dinos.dinos[dinosaur].health = team_dinos.dinos[dinosaur].health - 30
              print(f'{team_dinos.dinos[dinosaur].name} is too weak to attack! Lose health for trying!')
          elif team_robos.robots[dinosaur].health <= 0:
              team_robos.robots[dinosaur].health = 0
              team_dinos.dinos[dinosaur].attack_power = team_dinos.dinos[dinosaur].attack_power - 30
              print(f"{team_robos.robots[dinosaur].name} is gone to the emergency room. This is overkill!")
          elif team_dinos.dinos[dinosaur].health <= 0:
              team_dinos.dinos[dinosaur].health
              print(f"{team_dinos.dinos[dinosaur].name} is gone to the emergency room")
          else:
            team_robos.robots[dinosaur].health = team_robos.robots[dinosaur].health - team_dinos.dinos[dinosaur].attack_power
            team_dinos.dinos[dinosaur].attack_power = team_dinos.dinos[dinosaur].attack_power - 30
            team_dinos.dinos[dinosaur].attack(team_robos.robots[dinosaur].name)
        # return the inflicting damage done to the robot
        # the current robot stats will update 
      

        def robo_turn(self, robot):
    # return the inflicting damage done to the dinosaur
    # return the inflicting damage done to the dinosaur
    # the current dinosaur stats will update 
          if team_robos.robots[0].health + team_robos.robots[1].health + team_robos.robots[2].health <= 0:
              return 1
          elif team_robos.robots[robot].health <= 0:
              team_robos.robots[robot].health = 0
              team_robos.robots[robot].health = team_robos.robots[robot].health - 20
              print(f"{team_robos.robots[robot].name} is gone to the emergency room")
          else:
              team_dinos.dinos[robot].health = team_dinos.dinos[robot].health - team_robos.robots[robot].weapon.attack_power
              team_robos.robots[robot].attack(team_dinos.dinos[robot].name)
              print(f'{team_dinos.dinos[robot].name} was attacked with an {team_robos.robots[robot].weapon.name}')
   
        battle_over = False

        while battle_over == False:
            user_input = int(input("Enter 0, 1, 2 TO ATTACK ROBOS:  "))
            show_dino_opponent_option(self)
            user_input2 = int(input("Enter 0, 1, 2 TO ATTACK DINOS:  "))
            show_robo_opponent_option(self)
            if robo_turn(self, user_input2) == 1:
                battle_over = True  
                print(f"----TEAM DINO WINS----")
            elif dino_turn(self, user_input) == 0:
                battle_over = True
                print(f"----TEAM ROBO WINS----")

       
    
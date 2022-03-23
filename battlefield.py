from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
 
    def display_welcome(self):
        print("------Welcome to Robos vs. Dinos!!------")
        print("--------------Team Robos----------------")
        print("                  VS                    ")
        print("--------------Team Dinos----------------")

    def battle(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        team_robos = self.fleet
        team_dinos = self.herd

        def show_dino_opponent_option(self):
            print("------------------------------")
            for bots in team_robos.robots:
                print(f'{bots.name}, Health: {bots.health}, Attack Power: {bots.weapon.attack_power}')
            print("------------------------------")
    
        def show_robo_opponent_option(self):
            print("------------------------------")
            for dine in team_dinos.dinos:
                print(f'{dine.name}, Health: {dine.health}, Attack Power: {dine.attack_power}')
            print("------------------------------")
          
        def dino_turn(self, dinosaur):
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

        def robo_turn(self, robot):
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

       
    
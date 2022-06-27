from player import Player
from ai import AI
from human import Human

import time
import random


player_types_list = [Human, AI]

class Game:
    def __init__(self):
        self.rules_list = ["Rock crushes Scissors", "Scissors cuts Paper", "Paper covers Rock", "Rock crushes Lizard", "Lizard poisons Spock", "Spock smashes Scissors", "Scissors decapitates Lizard", "Lizard eats Paper","Paper disproves Spock", "Spock vaporizes Rock"]
        self.gestures_list = ["Choose 0 for Rock", "Choose 1 for Paper", "Choose 2 for Scissors", "Choose 3 for Lizard", "Choose 4 for Spock"]
        self.player_one = None
        self.player_two = None

#Everything needed to perfom the game       
    def run_game(self):

        self.display_welcome()
        self.display_rules()
        self.player_selection()
        self.game_mode()
        self.display_winner()

#Print Initial Welcome to Game
    def display_welcome(self):
        
        print("Welcome to Rock, Paper, Scissors, Lizard and Spock!")
        print("")
        print("Each match will be the best of three games.")
        print("")
        print("Use the number keys to enter your selection.")
        print("")

#Display Game Rules - Add sleep to slow text scroll
    def display_rules(self):      
        time.sleep(.5)
        print("Here are the Rules of the Game!")
        print("")
        time.sleep(.5)
        rules = [(time.sleep(.3), print(rule)) for rule in self.rules_list]
        print("")

#Player selection with logic to determine game type    
    def player_selection(self):
        user_input = input("How many players would you like? 1, 2 or 3 for a surprise ")
        self.user_input = user_input
        # self.human.type = human
        # self.ai.type = ai
        if user_input == "1":
            self.player_one = Human()
            self.player_two = AI()    
        elif user_input == "2":
            self.player_one = Human()
            self.player_two = Human()
        elif user_input == "3":
            self.player_one = AI() 
            self.player_two = AI()
        else:
            print("Please pick one of the choices")
            print("")
            user_input = input("How many players would you like? 1, 2 or 3 for a surprise ")
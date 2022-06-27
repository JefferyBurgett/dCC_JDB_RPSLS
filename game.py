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
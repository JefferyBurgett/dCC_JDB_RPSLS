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
import random

from player import Player
gestures_list = ["Choose 0 for Rock", "Choose 1 for Paper", "Choose 2 for Scissors", "Choose 3 for Lizard", "Choose 4 for Spock"]

class AI(Player):
    def __init__(self):
        super().__init__()
        
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'AI has picked  {self.chosen_gesture}')
        print("")
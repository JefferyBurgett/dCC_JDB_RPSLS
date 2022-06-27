class Player:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.display_options =  ["Choose 0 for Rock", "Choose 1 for Paper", "Choose 2 for Scissors", "Choose 3 for Lizard", "Choose 4 for Spock"]
        self.chosen_gesture =  ""
        self.wins = 0
from player import Player
import time

class Human(Player):
    def __init__(self):
        super().__init__()
        
        
    def choose_gesture(self):
            gestures = [(time.sleep(1), print(gesture)) for gesture in self.display_options]
            gesture_choice = int(input("Please select your gesture "))
            print("")
            self.chosen_gesture = self.gestures[gesture_choice]
            print(f'Player One has chosen {self.chosen_gesture}')
            print("")
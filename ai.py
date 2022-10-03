import random
from player import Player
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        

    def choose_gesture(self):
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = (random.choice(gesture_list))
        sleep(1)
        print(f'AI has chosen {self.chosen_gesture}')
import random
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.score = 0
        self.chosen_gesture = self.choose_gesture()

    def choose_gesture(self):
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = random.randrange(gesture_list (0,4))
        print(f'AI has chosen {self.chosen_gesture}')
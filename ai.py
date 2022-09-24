import random

class AI:
    def __init__(self, name):
        self.name = name
    def choose_gesture(self):
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = int(input('Please choose your gesture'))
        print(f'{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}')
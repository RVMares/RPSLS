from player import Player
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        
  
    
    def choose_gesture(self):
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        user_input=int(input(f'{self.name} please choose your gesture '))
        if user_input in [0, 1, 2, 3, 4]:
            self.chosen_gesture = gesture_list[user_input]
            print(f'{self.name} has chosen {self.chosen_gesture}')
        else:
            print ('That is not a valid option. Try again!')
            self.choose_gesture()


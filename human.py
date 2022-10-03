from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        
  
    
    def choose_gesture(self):
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        user_input=int(input(f'{self.name} please choose your gesture '))
        self.chosen_gesture = gesture_list[user_input]
        print(f'{self.name} has chosen {self.chosen_gesture}')
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.chosen_gesture = ""
    
    def choose_gesture(self):
        print('Choose 0 for Rock')
        print('Choose 1 for Paper')
        print('Choose 2 for Scissors')
        print('Choose 3 for Lizard')
        print('Choose 4 for Spock')
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        user_input=int(input('Please choose your gesture'))
        self.chosen_gesture = gesture_list[user_input]
        print(f'{self.name} has chosen {self.chosen_gesture}')
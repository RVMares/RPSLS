from human import Human
from ai import AI


class Rpsls_Platform:
    def __init__(self):
        self.player_one = Human('Player One')
        self.player_two = ""
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_players()
        winner = self.battle_phase()
        self.display_winner(winner)

    def display_welcome(self):
        print ('Welcome to RPSLS Player One!')
        print ('In a moment you will choose your opponent.')
        print ('I will explain the rules first.')
        print ('The name of the game is Rock, Paper, Scissors, Lizard, Spock.')
        print ('Or RPSLS for short.')
    
    def display_rules(self):
        print ('Rock crushes Scissors')
        print ('Scissors cuts Paper')
        print ('Paper covers Rock')
        print ('Rock crushes Lizard')
        print ('Lizard poisons Spock')
        print ('Spock smashes Scissors')
        print ('Scissors decapitates Lizard')
        print ('Lizard eats Paper')
        print ('Paper disproves Spock')
        print ('Spock vaporizes Rock')
    
    def choose_players(self):
        print ('For one player, press 1')
        print ('For two players, press 2')
        total_players = input ('How many players? ')
        if total_players == '1':
            self.player_two = AI('Player Two')
        elif total_players == '2':
            self.player_two = Human('Player Two')
        else:
            print ('That is not a valid option please press 1 or 2.')
            print (' ')
            self.choose_players()

    def battle_phase(self):
        print('Choose 0 for Rock')
        print('Choose 1 for Paper')
        print('Choose 2 for Scissors')
        print('Choose 3 for Lizard')
        print('Choose 4 for Spock')
        Human.choose_gesture(self)
         
    def display_winner(self):
        pass

    #Comparison if self.player_one.chosen_gesture = 'RocK" and self.player_two.choosen_gesture = "Paper" +1 self.player two score
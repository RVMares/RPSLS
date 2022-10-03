from human import Human
from ai import AI


class Rpsls_Platform:
    def __init__(self):
        self.player_one = Human('Player One')
        self.player_two = ''
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_players()
        winner = self.battle_phase()
        self.display_winner(winner)

    def display_welcome(self):
        print ('Welcome Player One!')
        print ('In a moment you will choose your opponent.')
        print ('I will explain the rules first.')
        print ('The name of the game is Rock, Paper, Scissors, Lizard, Spock!')
        print ('Or RPSLS for short.')
        print (' ')
    
    def display_rules(self):
        print ('First player to get 2 points wins the game!')
        print (' ')
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
        print (' ')
        print ('Use the number keys to make your choices')
        print (' ')
    
    def choose_players(self):
        print ('For one player, press 1')
        print ('For two players, press 2')
        total_players = input ('How many players? ')
        print (' ')
        if total_players == '1':
            self.player_two = AI('Player Two')
        elif total_players == '2':
            self.player_two = Human('Player Two')
        else:
            print ('That is not a valid option please press 1 or 2')
            print (' ')
            self.choose_players()

    def battle_phase(self):
        print('Choose 0 for Rock')
        print('Choose 1 for Paper')
        print('Choose 2 for Scissors')
        print('Choose 3 for Lizard')
        print('Choose 4 for Spock')
        print (' ')

        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            print (' ')
            self.player_two.choose_gesture()
            print (' ')
            if self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Paper':
                print ('Paper covers Rock')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Scissors':
                print ('Rock crushes Scissors')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Lizard':
                print ('Rock crushes Lizard')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Spock':
                print ('Spock vaporizes Rock')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1

            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Rock':
                print ('Paper covers Rock')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Scissors':
                print ('Scissors cuts Paper')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Lizard':
                print ('Lizard eats Paper')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Spock':
                print ('Paper disproves Spock')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Rock':
                print ('Rock crushes Scissors')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Paper':
                print ('Scissors cuts Paper')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Lizard':
                print ('Scissors decapitates Lizard')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Spock':
                print ('Spock smashes Scissors')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1

            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Rock':
                print ('Rock crushes Lizard')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Paper':
                print ('Lizard eats Paper')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Scissors':
                print ('Scissors decapitates Lizard')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Spock':
                print ('Lizard poisons Spock')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Rock':
                print ('Spock vaporizes Rock')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Paper':
                print ('Paper disproves Spock')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Scissors':
                print ('Spock smashes Scissors')
                print ('Player One wins this round!')
                print (' ')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Lizard':
                print ('Lizard poisons Spock')
                print ('Player Two wins this round!')
                print (' ')
                self.player_two.score += 1
            
            elif self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print ('This round is a tie!')
                print (' ')
                self.player_one.score += 0
                self.player_two.score += 0
            
            if self.player_one.score == 2 and self.player_two.score <2:
                return self.player_one
            elif self.player_two.score == 2 and self.player_one.score < 2:
                return self.player_two

         
    def display_winner(self, winner):
        print (f'{winner.name} Wins!')
        let_us_play_again = input ('Do you want to play again? Y/N ')
        if let_us_play_again == 'Y':
            self.run_game()
        else:
            print ('Goodbye!')

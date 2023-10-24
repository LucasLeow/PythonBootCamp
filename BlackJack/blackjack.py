import random
from blackjack_art import logo
import os

class BlackJack:
    pictures = ['J', 'Q', 'K']
    def __init__(self):
        self.deck = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.player_deck = []
        self.computer_deck = []
        self.player_score = 0
        self.computer_score = 0
        self.player_blk_jck = False
        self.computer_blk_jck = False
        self.player_ovr = False
        self.computer_ovr = False
    
    def generate_deck(self):
        for _ in range(2):
            self.player_deck.append(random.choice(self.deck))
            self.computer_deck.append(random.choice(self.deck))
            
    def compute_score(self):
        self.player_score = 0
        self.computer_score = 0

        for card in self.player_deck:
            if card in BlackJack.pictures:
                self.player_score += 10
            elif card == 'A' and (self.player_score + 11) <= 21:
                self.player_score += 11
            elif card == 'A':
                self.player_score += 1
            else:
                self.player_score += card

        for card in self.computer_deck:
            if card in BlackJack.pictures:
                self.computer_score += 10
            elif card == 'A' and (self.computer_score + 11) <= 21:
                self.computer_score += 11
            elif card == 'A':
                self.computer_score += 1
            else:
                self.computer_score += card

    def check_blk_jck(self):
        if self.player_score == 21:
            self.player_blk_jck = True
        if self.computer_score == 21:
            self.computer_blk_jck = True

    def check_ovr(self):
        if self.player_score > 21:
            self.player_ovr = True
        if self.computer_score > 21:
            self.computer_ovr = True


    def print_score(self):
        print(f'Your cards: {self.player_deck}, current score: {self.player_score}')
        print(f'Computer cards: {self.computer_deck}, computer score: {self.computer_score}')

    def check_status(self):

        self.check_blk_jck()
        self.check_ovr()

        if self.player_blk_jck and self.computer_blk_jck:
            print('Both BlackJack! Draw')
            return 1
        elif self.player_blk_jck:
            print('Player BlackJack. Congratulations, You Won!')
            return 1
        elif self.computer_blk_jck:
            print('Computer BlackJack. You Lost!')
            print(f'Computer cards: [{self.computer_deck[0]}, {self.computer_deck[1]}]')
            return 1

        if self.player_ovr and self.computer_ovr:
            print('Both over 21! Draw')
            return 1
        elif self.player_ovr:
            print('You exceeded 21. You Lost!')
            return 1
        elif self.computer_ovr:
            print('Computer exceeded 21. You Won!')
            return 1

        return 0

    def draw_card(self):
        usr_choice = input("Draw a card?: 'y' or 'n' ")
        if usr_choice == 'y':
            self.player_deck.append(random.choice(self.deck))
            return 1
        else:
            return 0

    def compare_final_scores(self):
        if self.player_score == self.computer_score:
            print('Game Tie!')
        elif self.player_score > self.computer_score:
            print(f'You Won by {self.player_score - self.computer_score} points')
        else:
            print(f'You lost by {self.computer_score - self.player_score} points')

        self.print_score()

if __name__ == '__main__':

    game_flag = True

    while (game_flag):
        play_again_flag = False
        usr_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
        if usr_choice == 'y':
            print(logo)
            game = BlackJack()
            game.generate_deck()
            game.compute_score()
            game.print_score()

            game_end = game.check_status()

            print(game_end)
            while not game_end:
                usr_draw_card = game.draw_card()
                if usr_draw_card:
                    game.compute_score()
                    game.print_score()
                    game_end = game.check_status()
                else:
                    game.compare_final_scores()
                    break

            while not play_again_flag:
                play_again = input("Play Again? 'y' or 'n' ")
                if play_again == 'y':
                    play_again_flag = True
                    game_flag = True
                    os.system('cls')

                elif play_again == 'n':
                    play_again_flag = True
                    game_flag = False
                    print('Have a nice day')
                else:
                    print("Invalid input. Please enter 'y' or 'n'")
                    continue


        elif usr_choice == 'n':
            print('Have a nice day.')
            break

        else:
            print("Invalid input. Please enter 'y' or 'n' ")
            continue









    
    


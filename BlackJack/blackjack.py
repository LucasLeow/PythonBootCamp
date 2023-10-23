import random
from blackjack_art import logo

class BlackJack:
    def __init__(self):
        self.deck = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] # 1 represent Ace
        self.player_deck = []
        self.computer_deck = []
    
    def generate_deck(self):
        for _ in range(2):
            self.player_deck.append(random.choice(self.deck))
            self.computer_deck.append(random.choice(self.deck))
            
    def compute_score(self):
                
        print(f'Your cards: [{self.player_deck[0]}, {self.player_deck[1]}], current score: ')

usr_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")

if usr_choice == 'y':
    print(logo)
    game = BlackJack()
    game.generate_deck()
    print(game.player_deck)
    print(game.computer_deck)
    
    


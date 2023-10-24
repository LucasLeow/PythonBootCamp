import random
from blackjack_art import logo

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
            elif card == 'A' and (self.player_score + 11) <= 21:
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
        self.compute_score()
        print(f'Your cards: [{self.player_deck[0]}, {self.player_deck[1]}], current score: {self.player_score}')
        print(f'Computer cards: [{self.computer_deck[0]}, {self.computer_deck[1]}, computer score: {self.computer_score}]')

        self.check_blk_jck()
        self.check_ovr()

        if self.player_blk_jck and self.computer_blk_jck:
            print("Both BlackJack! Draw")
        elif self.player_blk_jck:
            print('Player BlackJack. Congratulations, You Won!')
        elif self.computer_blk_jck:
            print('Computer BlackJack. You Lost!')
            print(f'Computer cards: [{self.computer_deck[0]}, {self.computer_deck[1]}]')


usr_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")

if usr_choice == 'y':
    print(logo)
    game = BlackJack()
    game.generate_deck()
    game.print_score()


    
    


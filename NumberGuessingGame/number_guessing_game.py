import random
from guess_art import logo

class GuessingGame:
    def __init__(self):
        self.difficulty = ''
        self.attempts = 0
        self.answer = 0
        
    def setup(self):
        print(logo)
        self.answer = random.randint(1, 100)
        print('Welcome to the Number Guessing Game!')
        print("I'm thinking of a number between 1 and 100.")

    def get_difficulty(self):
            valid = False
            while not valid:
                choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
                if choice == 'easy':
                    self.attempts = 10
                    break
                elif choice == 'hard':
                    self.attempts = 5
                    break
                else:
                    print("Invalid input. Please try again")
                    
    def start_game(self):
        while self.attempts:
            print(f"You have {self.attempts} remaining to guess the number")
            guess = int(input("Make a guess: "))
            
            if guess == self.answer:
                print(f"You got it! The answer was {self.answer}.")
                break
            
            elif guess > self.answer:
                if self.attempts > 1:
                    print('Too High.')
                    print('Guess again.')
                else:
                    print('Too High')
                self.attempts -= 1
                
            elif guess < self.answer:
                if self.attempts > 1:
                    print('Too Low.')
                    print('Guess again.')
                else:
                    print('Too Low')
                self.attempts -= 1
                
            if self.attempts == 0:
                print(f'You ran out of guesses! The answer was {self.answer}')
        
if __name__ == '__main__':
    play_again = True
    
    while play_again:
        
        game = GuessingGame()
        game.setup()
        game.get_difficulty()
        game.start_game()
        
        while True:
            choice = input("Play again? 'y' or 'n': ")
            if choice == 'y':
                break
            elif choice == 'n':
                play_again = False
                break
            else:
                print('invalid choice. Please try again')
                continue
    
    print("Thank you for playing. Have a nice day!")
import random
import os
from art import logo, vs
from collections import deque

class Celebrity:
    def __init__(self, name, follower_count, occupation, country):
        self.name = name
        self.follower_count = follower_count # follower_count in millions
        self.occupation = occupation
        self.country = country

class HigherLower:
    def __init__(self):
        self.score = 0
        self.queue = deque([])
        self.celebrities = [
            Celebrity('Cristiano Ronaldo', 607, 'Footballer', 'Portugal'),
            Celebrity('Lionel Messi', 488, 'Footballer', 'Argentina'),
            Celebrity('Selena Gomez', 430, 'Singer and Actress', 'USA'),
            Celebrity('Kylie Jenner', 400, 'Socialite and Media Personality', 'USA'),
            Celebrity('Dwayne "The Rock" Johnson', 392, 'Actor and Film Producer', 'USA'),
            Celebrity('Ariana Grande', 380, 'Singer-Songwriter and Actress', 'USA'),
            Celebrity('Kim Kardashian', 364, 'Media Personality and Socialite', 'USA'),
            Celebrity('Beyonce', 318, 'Singer-Songwriter and Businesswoman', 'USA'),
            Celebrity('Khloe Kardashian', 312,'Media Personality', 'USA'),
            Celebrity('Nike', 305,'Athletic Footwear & Apparel', 'USA'),
            Celebrity('Kendall Jenner', 294, 'Model & Media Personality', 'USA'),
            Celebrity('Justin Bieber', 293, 'Singer', 'Canada'),
            Celebrity('National Geographic', 283, 'Television network', 'USA'),
            Celebrity('Taylor Swift', 273, 'Singer-Songwriter', 'USA'),
            Celebrity('Virat Kohli', 260, 'Cricketer', 'India'),
            Celebrity( 'Jennifer Lopez', 252, 'Singer', 'USA'),
            Celebrity('Nicki Minaj', 227, 'Rapper and Singer-Songwriter', 'Trinidad'),
            Celebrity( 'Kourtney Kardashian', 224, 'Media Personality and Socialite', 'USA'),
            Celebrity('Miley Cyrus', 215, 'Singer-Songwriter and Actress', 'USA')
        ]
        
    def enqueue_celebs(self):
        self.queue.append(random.choice(self.celebrities))
        self.queue.append(random.choice(self.celebrities))
            
    def compare_initial(self):
        A = self.queue.popleft()
        B = self.queue.popleft()
        
        if A == B:
            self.enqueue_celebs()
            A = self.queue.popleft()
            B = self.queue.popleft()
        
        print(f'Compare A: {A.name}, a {A.occupation}, from {A.country}')
        print(vs)
        print(f'Against B: {B.name}, a {B.occupation}, from {B.country}')
        
        choice_flag = True
        while choice_flag:
            usr_choice = input("Who has more followers? Type 'A' or 'B': ")
            if usr_choice == 'A':
                if A.follower_count > B.follower_count:
                    self.score += 1
                    print(f"You're right! Current score: {self.score}")
                    return B
                else:
                    return None
            elif usr_choice == 'B':
                if B.follower_count > A.follower_count:
                    self.score += 1
                    print(f"You're right! Current score: {self.score}")
                    return B
                else:
                    return None
            else:
                print('invalid choice. please try again')
                continue
    
    def compare_next(self, winner):
        A = winner
        B = self.queue.popleft()
        if A == B:
            self.enqueue_celebs()
            B = self.queue.popleft()
        
        print(f'Compare A: {A.name}, a {A.occupation}, from {A.country}')
        print(vs)
        print(f'Against B: {B.name}, a {B.occupation}, from {B.country}')
        
        choice_flag = True
        while choice_flag:
            usr_choice = input("Who has more followers? Type 'A' or 'B': ")
            if usr_choice == 'A':
                if A.follower_count > B.follower_count:
                    self.score += 1
                    print(f"You're right! Current score: {self.score}")
                    return B
                else:
                    return None
            elif usr_choice == 'B':
                if B.follower_count > A.follower_count:
                    self.score += 1
                    return B
                else:
                    return None
            else:
                print('invalid choice. please try again')
                continue
                
    def compare_main(self):
        self.enqueue_celebs()
        winner = self.compare_initial()
        while winner:
            os.system('cls')
            print(logo)
            print(f"You're right! Current score: {self.score}")
            self.enqueue_celebs()
            winner = self.compare_next(winner)
        
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {self.score}")
        
if __name__ == '__main__':
    play_again = True

    while play_again:
        os.system('cls')
        print(logo)
        game = HigherLower()
        game.compare_main()
        
        while True:
            usr_choice = input("Play again? 'y' or 'n': ")
            if usr_choice == 'y':
                break
            elif usr_choice == 'n':
                play_again = False
                break
            else:
                print("invalid choice. please enter 'y' or 'n'")
                continue   
    
    print('Have a nice day')
    
import os
import time
from secretauction_logo import logo

class SecretAuction:
    def __init__(self, logo: str, bidders: dict):
        self.logo = logo
        self.bidders = bidders
    
    def get_bid(self):
        print(self.logo)
        print("Welcome to secret auction program")
        bid_flag = True
        
        while bid_flag:
            flag = None
            bidder = input("What is your name? ")
            if bidder in self.bidders:
                flag = self.bidder_exist(bidder)
            
            if flag == 0:
                continue
            elif flag == 1:
                continue_flag = self.get_rebid()
                if continue_flag:
                    os.system('cls')
                    continue
                else:
                    self.find_winner()
                    exit()

            else:
                bid_price = float(input("What's your bid? "))
                self.bidders[bidder] = bid_price
                continue_flag = self.get_rebid()
                if continue_flag:
                    os.system('cls')
                    continue
                else:
                    self.find_winner()
                    exit()

    def bidder_exist(self, bidder):
        while True:
            usr_decision = input("Name already registered, update value? yes / no: ")
            if usr_decision not in ['yes', 'no']:
                print('invalid input, please enter yes or no')
                continue
            else:
                if usr_decision == 'yes':
                    bid_price = float(input("What's your new bid? "))
                    self.bidders[bidder] = bid_price
                    return 1
                else:
                    print("Please enter another unique name")
                    time.sleep(2)
                    os.system('cls')
                    return 0
                
    def get_rebid(self):
        while True:
            usr_input = input("Are there any other bidders? 'yes' or 'no' \n")
        
            if usr_input not in ['yes', 'no']:
                print("invalid input")
                continue
            
            else:
                if usr_input == 'yes':
                    return 1
                else:
                    return 0
                
    def find_winner(self):
        top_bidder = max(self.bidders, key=self.bidders.get)
        print(f"The winner is {top_bidder} with a bid of ${self.bidders[top_bidder ]}")
            
        
sa = SecretAuction(logo, {})
sa.get_bid()
        
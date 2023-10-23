import os
import time
from Day10_calculatorlogo import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

outer_flag =  True
inner_flag = True


while outer_flag:
    print(logo)
    try:
        first_num = float(input("What's the first number?: "))
        for char in operations.keys():
            print(char)

        ops = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))

        while inner_flag:
            try:
                results = operations[ops](first_num, second_num)
                print(f"{first_num} {ops} {second_num} = {results}")
                user_choice = input(f"Type 'y' to continue calculating with {results}, or type 'n' to start new calculation: " )
                if user_choice == 'y':
                    first_num = results
                    ops = input("Pick an operation: ")
                    second_num = float(input("What's the next number?: "))
                elif user_choice == 'n':
                    break
            except KeyError:
                print("Unknown operator selected. Please try again")
                time.sleep(1)
                for char in operations.keys():
                    print(char)
                ops = input("Pick an operation: ")
                continue
        os.system('cls')
    except KeyError:
        print("Unknown operator selected. Please try again")
        time.sleep(1)
        for char in operations.keys():
            print(char)
        ops = input("Pick an operation: ")
        continue


# class Calculator:
#     def __init__(self):
#         self.first_num = None
#         self.second_num = None
#         self.ops = None
#         self.
    
#     def get_inputs(self):
#         self.first_num = float(input("What's the first number?"))
#         self.print_ops()
#         self.ops = input("Pick an operation")
#         self.second_num = float(input("Whats the next number?"))
        
#     def calculate(self):
#         if self.ops == '+':
            
#     def print_ops(self):
#         for ops in self.operations:
#             print(ops)
        
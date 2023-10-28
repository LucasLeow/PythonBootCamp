from menu import *

money = 0
money_earned = 0

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_earned}")

def get_money():
    print('Please insert coins.')
    for coin_type in coins.keys():
        num_coin = int(input(f'How many {coin_type}?: '))
        coins[coin_type] = num_coin

    total = coins['quarters'] * 0.25 + coins['dimes'] * 0.1 + coins['nickels'] * 0.05 + coins['pennies'] * 0.01
    return total


def check_resource(coffee_type, cur_resource):
    for ingredient_type, required_amt in MENU[coffee_type]['ingredients'].items():
        if cur_resource[ingredient_type] - required_amt < 0:
            return ingredient_type
    return True

def deduct_resource(coffee_type, cur_resource):
    for ingredient_type, required_amt in MENU[coffee_type]['ingredients'].items():
        cur_resource[ingredient_type] -= required_amt

machine_on = True
while machine_on:
    usr_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if usr_choice == 'report':
        print_report()
    elif usr_choice == 'espresso' or usr_choice == 'latte' or usr_choice == 'cappuccino':
        sufficient = check_resource(usr_choice, resources)
        if sufficient == True:
            money = get_money()
            if money < MENU[usr_choice]['cost']:
                print("Sorry, that's not enough money. Money refunded.")
                money = 0
            else:
                deduct_resource(usr_choice, resources)
                change = money - MENU[usr_choice]['cost']
                money_earned += MENU[usr_choice]['cost']
                money = 0
                print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {usr_choice} ☕. Enjoy! ")
        else:
            print(f"Sorry there is not enough {sufficient}.")
    elif usr_choice == 'off':
        machine_on = False

print('Coffee Machine turned off.')






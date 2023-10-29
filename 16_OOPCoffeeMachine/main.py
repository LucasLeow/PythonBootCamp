from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    machine_on = True
    coffee_machine = CoffeeMaker()
    coffee_menu = Menu()
    money_machine = MoneyMachine()

    while machine_on:
        usr_input = input(f"What would you like? ({coffee_menu.get_items()}): ")

        if usr_input == 'report':
            coffee_machine.report()
            money_machine.report()

        elif usr_input == 'off':
            machine_on = False
            print('Coffee Machine turned off.')
            break

        else:
            desired_coffee = coffee_menu.find_drink(usr_input)
            sufficient = coffee_machine.is_resource_sufficient(desired_coffee)
            if sufficient:
                money_sufficient = money_machine.make_payment(desired_coffee.cost)
                if money_sufficient:
                    coffee_machine.make_coffee(desired_coffee)



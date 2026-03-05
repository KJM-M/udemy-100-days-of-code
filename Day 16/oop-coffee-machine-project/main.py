from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True


while is_machine_on:
    options = menu.get_items()

    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
            if money_machine.make_payment(menu.find_drink(choice).cost):
                coffee_maker.make_coffee(menu.find_drink(choice))

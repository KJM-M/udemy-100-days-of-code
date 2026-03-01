from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300, #300
    "milk": 200, #200
    "coffee": 100, #100
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}


def check_needed_resources(resources, coffee_choice):
    for ingredient in MENU[coffee_choice]["ingredients"]:
        if MENU[coffee_choice]["ingredients"][ingredient]> resources[ingredient]:
            print(f"There's not enough {ingredient} in the machine atm. Sorry.")
            return False
    return True


def process_coins(inserted_coins, coffee_choice):
    print(f"That's total {MENU[coffee_choice]["cost"]}$. Please insert coins.")
    inserted_quarters = float(input("How many quarters?: "))
    inserted_coins += (inserted_quarters * coins["quarter"])
    inserted_dimes = float(input("How many dimes?: "))
    inserted_coins += (inserted_dimes * coins["dime"])
    inserted_nickels = float(input("How many nickels?: "))
    inserted_coins += (inserted_nickels * coins["nickel"])
    inserted_pennies = float(input("How many pennies?: "))
    inserted_coins += (inserted_pennies * coins["penny"])
    return inserted_coins

print(logo)

while True:
    coffee_choice = str(input("\nWhat would you like? (espresso/latte/cappuccino): ")).lower()
    change = 0
    inserted_coins = 0

    if coffee_choice == "off":
        exit()
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
    elif coffee_choice == "latte" or coffee_choice == "cappuccino" or coffee_choice == "espresso":
        if check_needed_resources(resources, coffee_choice):
            inserted_coins = process_coins(inserted_coins, coffee_choice)
            if inserted_coins >= MENU[coffee_choice]["cost"]:
                change = inserted_coins - MENU[coffee_choice]["cost"]
                for ingredient in MENU[coffee_choice]["ingredients"]:
                    resources[ingredient] -= MENU[coffee_choice]["ingredients"][ingredient]
                print(f"Here's your {coffee_choice} ☕️ Enjoy!")
                print(f"Here is ${round(change, 2)} in change.")
            else:
                print("Sorry that's not enough money. Money refunded")

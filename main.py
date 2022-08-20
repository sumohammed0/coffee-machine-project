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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def ask_user():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return user_choice


def check_resources(chosen_drink):
    water = MENU[chosen_drink]["ingredients"]["water"]
    coffee = MENU[chosen_drink]["ingredients"]["coffee"]
    if chosen_drink == "espresso":
        milk = 0
    else:
        milk = MENU[chosen_drink]["ingredients"]["milk"]
    if resources["water"] >= water and resources["milk"] >= milk and resources["coffee"] >= coffee:
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        return True
    else:
        return False

# print there isn't enough for each individual resource


def check_money(chosen_drink, money_given):
    cost_of_drink = MENU[chosen_drink]["cost"]
    if money_given > cost_of_drink:
        resources["money"] = cost_of_drink
        change = money_given - cost_of_drink
        change = round(change, 3)
        print(f"Here's your change: {change}")
        return True
    elif money_given == cost_of_drink:
        resources["money"] = cost_of_drink
        return True
    else:
        return False


def enter_coins():
    print("Please enter coins.")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies?: "))
    return quarters + nickles + dimes + pennies


def make_drink(chosen_drink):
    if chosen_drink == "report":
        return resources
    enough_resources = check_resources(chosen_drink=chosen_drink)
    if enough_resources:
        money_given = enter_coins()
        enough_money = check_money(chosen_drink=chosen_drink, money_given=money_given)
        if enough_money:
            return f"Here's your {chosen_drink} enjoy!"
        else:
            return "Sorry that's not enough money. Money has been refunded. "
    else:
        return "Sorry there isn't enough resources."


def print_report():
    print(resources)


ask_again = True
drink = ask_user()

if drink == "off":
    ask_again = False

while ask_again:
    can_make = make_drink(chosen_drink=drink)
    print(can_make)
    drink = ask_user()
    if drink == "off":
        ask_again = False

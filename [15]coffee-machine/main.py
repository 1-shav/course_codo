menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 500,
    "milk": 400,
    "coffee": 250,
    "money" : 0
}



def check_resources(water, milk, coffee):
    """Checks if enough resources are available for making coffee"""
    if resources["water"] >= water and resources["milk"] >= milk and resources["coffee"] >= coffee:
        return True
    else:
        return False
    

def recieve_money(coffee):
    """Recieves coins and returns actual amount recieved"""
    print(f"That will be ${menu[coffee]['cost']}.\nPlease insert coins.")
    quaters = int(input("how many quaters? :"))
    dimes = int(input("how many dimes? :"))
    nickles = int(input("how many nickles? :"))
    pennies = int(input("how many pennies? :"))
    money_received = (quaters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return money_received


def update_resources(coffee, amount_received):
    """Checks if money recieved is enough, refunds if it is excess and updates all variables"""
    cost = menu[coffee]["cost"]
    if cost == amount_received:
        print(f"Here is your {coffee}. Enjoy!")
        resources["water"] -= menu[coffee]["ingredients"]["water"]
        resources["milk"] -= menu[coffee]["ingredients"]["milk"]
        resources["coffee"] -= menu[coffee]["ingredients"]["coffee"]
        resources["money"] += cost

    elif cost < amount_received:
        money_returned = amount_received - cost
        print(f"Here is ${round(money_returned, 2)} in change.\nAnd here is your {coffee}. Enjoy!")
        resources["water"] -= menu[coffee]["ingredients"]["water"]
        resources["milk"] -= menu[coffee]["ingredients"]["milk"]
        resources["coffee"] -= menu[coffee]["ingredients"]["coffee"]
        resources["money"] += cost
        return True
    elif cost > amount_received:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def whats_short(water, milk, coffee,):
    """Checks what is not sufficient"""
    if water > resources["water"]:
        print("Error 69: Sorry there is not enough water. Money Refunded")
    elif milk > resources["milk"]:
        print("Error 99: Sorry there is not enough milk. Money Refunded")
    elif coffee > resources["coffee"]:
        print("Error 09: Sorry there is not enough coffee. Money Refunded")


while True:
    choice = input("What would you like to have? [espresso/latte/cappuccino]: ").lower()

    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}g\nMoney: ${round(resources['money'], 2)}")
    else:
        if choice == "espresso":
            if check_resources(menu["espresso"]["ingredients"]["water"], menu["espresso"]["ingredients"]["milk"], menu["espresso"]["ingredients"]["coffee"]):
                amount = recieve_money(choice)
                update_resources(choice, amount)
            else:
                whats_short(menu["espresso"]["ingredients"]["water"], menu["espresso"]["ingredients"]["milk"], menu["espresso"]["ingredients"]["coffee"])
        elif choice == "latte":
            if check_resources(menu["latte"]["ingredients"]["water"], menu["latte"]["ingredients"]["milk"], menu["latte"]["ingredients"]["coffee"]):
                amount = recieve_money(choice)
                update_resources(choice, amount)
            else:
                whats_short(menu["latte"]["ingredients"]["water"], menu["latte"]["ingredients"]["milk"], menu["latte"]["ingredients"]["coffee"])
        elif choice == "cappuccino":
            if check_resources(menu["cappuccino"]["ingredients"]["water"], menu["cappuccino"]["ingredients"]["milk"], menu["cappuccino"]["ingredients"]["coffee"]):
                amount = recieve_money(choice)
                update_resources(choice, amount)
            else:
                whats_short(menu["cappuccino"]["ingredients"]["water"], menu["cappuccino"]["ingredients"]["milk"], menu["cappuccino"]["ingredients"]["coffee"])
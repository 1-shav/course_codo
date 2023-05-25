from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()
maker = CoffeeMaker()
paisa = MoneyMachine()
while True:
    choice = input(f"What would you like to have? [{item.get_items()}]: ").lower()
    if choice == "off":
        break
    elif choice == "report":
        maker.report()
        paisa.report()
    else:
        item_info = item.find_drink(choice)
        if item_info != None:
            if maker.is_resource_sufficient(item_info):
                print(f"That will be ${item_info.cost}")
                if paisa.make_payment(item_info.cost):
                    maker.make_coffee(item_info)
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    print(f"this is the available drink {menu.get_items()}")
    user_drink = input("Would you like to drink? ").lower()

    if user_drink == "report":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(user_drink):
        minuman = menu.find_drink(user_drink)
        print(minuman.cost)
        resources = coffee_maker.is_resource_sufficient(minuman)
        if resources:
            payment = money_machine.make_payment(minuman.cost)
            if payment:
                coffee_maker.make_coffee(minuman)

    elif user_drink == "off":
        break


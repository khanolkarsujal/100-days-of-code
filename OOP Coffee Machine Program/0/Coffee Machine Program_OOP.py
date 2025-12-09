from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    user_choice = input(f"What would you like? {menu.get_items()} : ").lower()

    # turn machine off
    if user_choice == "off":
        machine_on = False
        continue

    # show report
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    # STEP 1: find drink
    drink = menu.find_drink(user_choice)

    # if drink not available → stop this loop iteration
    if drink is None:
        print("That drink is not on the menu.")
        continue

    # STEP 2: check resources
    if not coffee_maker.is_resource_sufficient(drink):
        print("Not enough resources.")
        continue

    # STEP 3: handle payment
    print(f"The cost is ${drink.cost}.")
    if not money_machine.make_payment(drink.cost):
        print("Payment not accepted. Try again.")
        continue

    # STEP 4: make the drink
    coffee_maker.make_coffee(drink)

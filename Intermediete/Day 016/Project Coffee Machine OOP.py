from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_off = False
while not coffee_machine_off:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        print("Turning off the coffee machine")
        coffee_machine_off = True
    else:
        coffee = menu.find_drink(user_choice)
        if coffee is not None:
            if coffee_maker.is_resource_sufficient(coffee): # check the resource
                if money_machine.make_payment(coffee.cost): # process the payment
                    coffee_maker.make_coffee(coffee) # make the coffee

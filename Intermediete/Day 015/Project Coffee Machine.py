from database import resources, MENU

def checking_resources(coffee):
    """checking resources function to check if the resources are sufficient for the coffee."""
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return False
    elif resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True

def payment():
    """payment function to process the payment and return the total amount received."""
    while True:
        try:
            print("please insert coins")
            quarter = int(input("how many quarter?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total = quarter * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            return total
        except ValueError:
            print("Wrong input, please enter a valid number.")

def update_resources(coffee):
    """making coffee function to prepare the coffee and update the resources."""
    resources["money"] += MENU[coffee]["cost"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

def process_order(coffee):
    """full cycle function to handle the entire cycle of making coffee.
    from checking resources to making coffee and payment."""
    resources_status = checking_resources(coffee)  # checking resources
    if resources_status:
        total = payment()  # ask for payment
        if total >= MENU[coffee]["cost"]:
            if total > MENU[coffee]["cost"]:
                change = total - MENU[coffee]["cost"]  # give change
                print(f"Here is ${change} in change.")
            update_resources(coffee)
            print(f"here is your {coffee} ☕️. Enjoy")
        else:
            print("Sorry that's not enough money. Money refunded.")

def report():
    """report function to display the current resources."""
    water = resources["water"]
    milk = resources["milk"]
    coffee_beans = resources["coffee"]
    money = resources["money"]
    print(f"The current resources is:\nwater: {water}\nmilk: {milk}\ncoffee: {coffee_beans}\nmoney: {money}")

coffee_machine_off = False
while not coffee_machine_off:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        process_order(coffee)
    elif coffee == "report":
        report()
    elif coffee == "off":
        print("Turning off the coffee machine")
        coffee_machine_off = True
    else:
        print("Invalid input. Please try again.")
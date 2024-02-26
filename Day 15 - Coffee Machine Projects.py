# coffee machine projects

MENU = {
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_total = 0

coins = {
    "Penny": .01,
    "Nickel": .05,
    "Dime": .10,
    "Quarter": .25,
}


def paying(cost):
    pennies = int(input("How many pennies are you inserting? "))
    nickles = int(input("How many nickles are you inserting? "))
    dimes = int(input("How many dimes are you inserting? "))
    quarters = int(input("How many quarters are you inserting? "))
    total_change = (pennies*.01 + nickles*.05 + dimes*.1 + quarters*.25)
    amount_returned = round(total_change-cost, 2)
    if total_change == cost:
        print("Thanks! You gave the exact amount of change.")
        return cost
    elif total_change > cost:
        print(f"Thanks your change is ${amount_returned}.")
        return cost
    else:
        print("You did not give enough money. Your change is being returned.")
        cost = 0
        return cost


def remaining_resources(coffee):
    resources["water"] = resources["water"] - MENU[coffee]['ingredients']['water']
    resources["milk"] = resources["milk"] - MENU[coffee]['ingredients']['milk']
    resources["coffee"] = resources["coffee"] - MENU[coffee]['ingredients']['coffee']


def coffee_amount(coffee):
    print(f"You owe ${MENU[coffee]['cost']}")
    return MENU[coffee]['cost']


#  ingredient check
def ingredient_check(choice):
    if choice == "report":
        return True
    elif MENU[choice]['ingredients']['water'] <= resources["water"] \
            and MENU[choice]['ingredients']['milk'] <= resources["milk"] \
            and MENU[choice]['ingredients']['coffee'] <= resources["coffee"]:
        return True
    else:
        return False


machine_running = True
while machine_running:
    coffee_selection = input("What would you like to order today? (Espresso/Latte/Cappuccino)\n").lower()
    if coffee_selection == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]} ml")
        print(f"${machine_total}")
        turn_off_machine = input("Would you like to order more?(y or n)\n").lower()
    else:
        if ingredient_check(coffee_selection):
            amount = coffee_amount(coffee_selection)
            remaining_resources(coffee_selection)
            amount_paid = paying(amount)
            machine_total += amount_paid
            if amount_paid == 0:
                machine_running = False
                turn_off_machine = "y"
            else:
                turn_off_machine = input("Would you like to order more?(y or n)\n").lower()
        else:
            machine_running = False
            print("Sorry there isn't enough ingredients to make your drink. Have a nice day!")
    if turn_off_machine == "y" and machine_running:
        machine_running = True
    else:
        machine_running = False
        print("Thanks for ordering! Have a nice day!")


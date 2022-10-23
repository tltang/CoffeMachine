# import replit
# #
# # from replit import clear

import constants

def report():
    print(f"Water: {constants.resources['water']}ml")
    print(f"Milk: {constants.resources['milk']}ml")
    print(f"Coffee: {constants.resources['coffee']}g")
    print(f"Money: ${dMoney}")
    # cMoney = constants.resources["balance"]

def checkBalance(cDrink):
    for item in cDrink:
        # print(item)
        # print(cDrink[item])
        # print(constants.resources[item])
        if cDrink[item] > constants.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return "No resource"

def checkMoney(cChoice):
    dCost1 = constants.MENU[cChoice]["cost"]
    print("Please insert coins.")
    iQuarter = int(input("How many quarters? "))
    iDime = int(input("How many dimes? "))
    iNickle = int(input("How many nickles? "))
    iPenny = int(input("How many pennies? "))
    dPayment = iQuarter * .25 + iDime * .1 + iNickle * .05 + iPenny * .01

    if dPayment < dCost1:
        print("Sorry that's not enough money. Money refunded.")
        return -1
    else:
        return dPayment

def MakeCoffee(choice, drink, dPayment):
    dCost1 = drink["cost"]

    global dMoney

    cIngredients = drink["ingredients"]

    for item in cIngredients:
        constants.resources[item] = constants.resources[item] - cIngredients[item]

    dMoney = dMoney + dCost1

    if dPayment > dCost1:
        dChange = round(dPayment - dCost1, 2)
        print(f"Here is ${dChange} dollars in change.")

    print(f"Here is your {choice}, Enjoy!")

dMoney = 0.0
lContinue = True

while lContinue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
        lContinue = False
    elif choice == 'report':
        report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = constants.MENU[choice]
        cResource = checkBalance(drink["ingredients"])
        if cResource is None:
            dPayment = checkMoney(choice)
            if dPayment != -1:
                MakeCoffee(choice, drink, dPayment)
    else:
        print(f"{choice} is not a valid choice")
    #         "cost": 1.5,
    #     },




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

#MONEY
money = 0


machine_is_on = True
while machine_is_on :

    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    #Turn off the Coffee Machine
    if user_choice == "off":
        machine_is_on = False

    #Print report.
    elif user_choice == "report":
        for element in resources:
            print(f"{element}: {resources[element]}")
        print(f"Money: ${money}")    

    #Check resources sufficient?
    elif user_choice in MENU:
        resources_ok = True
        for item,amount in MENU[user_choice]["ingredients"].items():
            if amount > resources[item]:
                print(f"Sorry there is not enough {item}.")
                resources_ok = False
                break
        if resources_ok:
            print("Resources OK! Proceeding to payment...")
            #Ask for coins
            total = int(input("How many quarters?: ")) * 0.25
            total += int(input("How many dimes?: ")) * 0.10
            total += int(input("How many nickels?: ")) * 0.05
            total += int(input("How many pennies?: ")) * 0.01

            drink_cost = MENU[user_choice]["cost"]
            
            if drink_cost > total:
                print("Sorry that's not enough money. Money refunded.")
            else:

                new_total = round(total - drink_cost,2)
                print(f"Here is your change ${new_total}")



                #money
                money += drink_cost

                #deduct money
                for item,amount in MENU[user_choice]["ingredients"].items():
                    resources[item] -= amount



                print(f"Here is your {user_choice} ☕ Enjoy!")
                        

    
     
  
    else:
        print("Invalid Input")    
    








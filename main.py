# Day 15 Project
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


# TODO: 1. Prompt the user by asking what they would like
def prompt_user():
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # TODO: 3. Print report of coffee machine resources
        if user_choice == "report":
            for key in resources:
                print(f"{key}: {resources[key]}")
            break
        elif user_choice == "espresso":
            break
        elif user_choice == "latte":
            break
        elif user_choice == "cappuccino":
            break
        # TODO: 2. Turn off coffee machine by entering off to the prompt
        elif user_choice == "off":
            break
        else:
            print("Error! Please enter one of the options!")
    return user_choice


# TODO: 4. Check if resources are sufficient
def enough_resources(user_input, current_resources):
    for resource in MENU[user_input]["ingredients"]:
        if MENU[user_input]["ingredients"][resource] > current_resources[resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    else:
        return True


# TODO: 5. Process coins
def check_coins(input_user):
    print("Please insert coins.")
    quarters = (25 * int(input("Enter the amount of quarters: "))) / 100
    dimes = (10 * int(input("Enter the amount of dimes: "))) / 100
    nickels = (5 * int(input("Enter the amount of nickels: "))) / 100
    pennies = (int(input("Enter the amount of pennies: "))) / 100
    total = quarters + dimes + nickels + pennies

    # TODO: 6. Check if transaction was successful
    if total < MENU[input_user]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - MENU[input_user]["cost"], 2)
        print(f"Here is your ${change} in change.")
        return True


# TODO: 7. Make coffee
# If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.

# Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
# If latte was their choice of drink.
def make_coffee(input_user, enough_r):
    global resources
    for resource in MENU[input_user]["ingredients"]:
        if enough_r:
            resources[resource] = resources[resource] - MENU[input_user]["ingredients"][resource]
    print(f"Here is your {input_user}! Enjoy!")


machine_running = True
current_resources = resources
while machine_running:
    user_input = prompt_user()
    if user_input == "off":
        machine_running = False
    else:
        resource_check = enough_resources(user_input, current_resources)
        if resource_check:
            transaction_made = check_coins(user_input)
            if transaction_made:
                make_coffee(user_input, resource_check)




import menu
import resources

def report():
    """Prints the current state of coffee machine resources 
    (water, milk, coffee) and accumulated money."""
    print(f"Water: {resources.resources["water"]}ml")
    print(f"Milk: {resources.resources["milk"]}ml")
    print(f"Coffee: {resources.resources["coffee"]}g")
    print(f"Money: ${round(resources.resources["money"], 2)}")


def coins(q, d, n, p):
    """Calculates the total value of inserted coins 
    (quarters, dimes, nickels, pennies) in dollars."""
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    return q * quarters + d * dimes + n * nickles + p * pennies

def update_resources(drink):
    """Subtracts the required ingredients for the selected 
    drink from the coffee machine's resources."""
    ingredients = menu.MENU[drink]["ingredients"]
    resources.resources["water"] -= ingredients["water"]
    resources.resources["coffee"] -= ingredients["coffee"]
    if "milk" in ingredients:
        resources.resources["milk"] -= ingredients["milk"]


def user_coin_check(coin):
    """Validates that the user input 
    for a coin type is a positive integer."""
    while True:
        try:
            user_guess = int(input(f"{coin}:"))
            if user_guess >= 0:
                return user_guess
            print("The number should be greater then 0!")
        except ValueError:
            print("The answer should be a number!")
            continue

while True:
    user_answer = input("What would you like? (espresso/latte/cappuccino):")
    if user_answer == "off":
         break
    while user_answer not in ["espresso", "latte", "cappuccino", "report"]:
        print("You supposed to pick up the drink! Try again!")
        user_answer = input("What would you like? (espresso/latte/cappuccino):")
    if user_answer == "report":
        report()
        continue
    ingredients = menu.MENU[user_answer]["ingredients"]
    if resources.resources["water"] - menu.MENU[user_answer]["ingredients"]["water"] < 0:
            print("Sorry there is not enough water.")
            continue
    elif resources.resources["coffee"] - menu.MENU[user_answer]["ingredients"]["coffee"] < 0:
            print("Sorry there is not enough coffee.")
            continue
    elif ("milk" in ingredients) and resources.resources["milk"] - menu.MENU[user_answer]["ingredients"]["milk"] < 0:
            print("Sorry there is not enough milk.")
            continue 
    else:
        print("Insert coins")
       
        quarters = user_coin_check("quarters")
        dimes = user_coin_check("dimes")
        nickles = user_coin_check("nickels")
        pennies = user_coin_check("pennies")

        result = coins(quarters, dimes, nickles, pennies)
        if result > menu.MENU[user_answer]["cost"]:
            in_change = result - menu.MENU[user_answer]["cost"]
            resources.resources["money"] += menu.MENU[user_answer]["cost"]
            print(f"Here is ${round(in_change, 2)} dollars in change.")
        elif result == menu.MENU[user_answer]["cost"]:
              resources.resources["money"] += menu.MENU[user_answer]["cost"]
        elif result < menu.MENU[user_answer]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        update_resources(user_answer)
        report()
        print(f"Enjoy your {user_answer}!")
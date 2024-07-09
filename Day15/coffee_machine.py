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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resourse_sufficient(order_ingredients):
    for key in order_ingredients:
        if order_ingredients[key]>=resources[key]:
            print("Coffee ingredients are not sufficient")
            return False

    return True

def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on=True
while is_on:
    choice=input( "What would you like? (espresso/latte/cappuccino/report):").lower()
    if choice=='off':
        is_on=False
    elif choice=='report':
        for key in resources:
            print(f"{key}:{resources[key]} ml")
        print(f"Money:{profit}")
    else:
        drink=MENU[choice]
        if is_resourse_sufficient(drink["ingredients"]):
            payment=process_coin()
        if transaction_successful(payment,drink["cost"]):
            make_coffee(choice,drink["ingredients"])

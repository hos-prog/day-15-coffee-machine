#Hosama adem
from tkinter import Menu

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


quarter=0.25
dime=0.1
nickle=0.05
penny=0.01
Money=0
birr=0


#Todo 1 :-print report
def display_report():
    print(f"water : {resources['water']}ml")
    print(f"milk : {resources['milk']}ml")
    print(f"coffee : {resources['coffee']}g")
    print(f"Money: ${round(birr,2)}")


#Todo 2:- coins checking funuction
def ask_coins():
    q=int(input("How Many Quarters?: "))
    d=int(input("How Many dimes?: "))
    n=int(input("How Many nickles?: "))
    p=int(input("How Many pennies?: "))
    global Money
    Money += ((q * quarter) + (d * dime) + (n * nickle) + (p * penny))
    return Money


#Todo 3:- looping with the condition
go_head=False
while not go_head:
    user=input("What would you like ?(espresso/latte/cappuccino): ").lower()
    if user == "espresso":
        if resources['water'] >=MENU["espresso"]["ingredients"]['water'] and resources['coffee'] >= MENU["espresso"]["ingredients"]['coffee'] :
            ask_coins()
            if Money < MENU["espresso"]["cost"]:
                print("sorry, you don't have enough money")
                continue
            else:
                print(f"Here is $ {round(Money - (MENU["espresso"]["cost"]), 3)} in change ")
                birr
                birr += (Money - (MENU["espresso"]["cost"]))

                print("Here is your esperesso Enjoy!")
                resources["water"] -= MENU["espresso"]["ingredients"]['water']
                resources['coffee'] -= MENU["esperesso"]["ingredients"]['coffee']

        else:
            print("sorry, the resourses is not availabile")
            continue


#if user types to get latte

    elif user == "latte":
        if resources['water'] >= MENU["latte"]["ingredients"]['water'] and resources['coffee'] >= MENU["latte"]["ingredients"]['coffee']  :
            if resources['milk'] >= MENU["latte"]["ingredients"]['milk']:
                ask_coins()
                if Money<MENU["latte"]["cost"]:
                    print("sorry, you don't have enough money")
                    continue
                else:
                    print(f"Here is $ {round(Money-(MENU["latte"]["cost"]),3)} in change ")
                    birr
                    birr+=(Money-(MENU["latte"]["cost"]))
                    print("Here is your latte Enjoy!")
                    resources["water"] -= MENU["latte"]["ingredients"]['water']
                    resources['coffee'] -= MENU["latte"]["ingredients"]['coffee']
                    resources['milk'] -= MENU["latte"]["ingredients"]['milk']
            else:
                print("sorry, the resourses is not availabile")
                continue


#if user wants cappuccino
    elif user == "cappuccino":
        if resources['water'] >= MENU["cappuccino"]["ingredients"]['water'] and resources['coffee'] >= MENU["cappuccino"]["ingredients"]['coffee'] :
            if resources['milk'] >= MENU["cappuccino"]["ingredients"]['milk']:
                ask_coins()
                if Money < MENU["cappuccino"]["cost"]:
                    print("sorry, you don't have enough money")
                    continue
                else:
                    print(f"Here is $ {round((MENU["cappuccino"]["cost"]),3)} in change ")
                    birr
                    birr += (Money - (MENU["cappuccino"]["cost"]))
                    print("Here is your cappuccino Enjoy!")
                    resources["water"] -= MENU["cappuccino"]["ingredients"]['water']
                    resources['coffee']-=MENU["cappuccino"]["ingredients"]['coffee']
                    resources['milk']-=MENU["cappuccino"]["ingredients"]['milk']
            else:
                print("sorry, the resourses is not availabile")
                continue


# if user wants  to quite
    elif user =="off":
        print("good bye every body every body")
        go_head=True


# if user wants to know the report
    elif user=='report':
        display_report()



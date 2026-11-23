import random
menu = ["Burger", "Fries", "Pizza", "Soda"]
prices = [8, 3, 10, 2]   # same order as menu
cart = []


def specials():
    random_special = random.choice(menu)
    while True:
        hear_specials = input("Would you like to hear todays specials? Y/N ")
        if hear_specials == "Y":
            break
        elif hear_specials == "N":
            return
        else:
            print("Please give a Y or N ")
    if random_special == "Burger":
        print(f"Today's Special is {menu[0]} for ${prices[0]}")
    elif random_special == "Fries":
        print(f"Today's Special is {menu[1]} for ${prices[1]}")
    elif random_special == "Pizza":
        print(f"Today's Special is {menu[2]} for ${prices[2]}")
    else:
        print(f"Today's Special is {menu[3]} for ${prices[3]}")
    return random_special

def find_menu(item, menu):
    return item in menu if menu else None

def show_menu(menu, prices, today_specials):
    for item in menu:
        print(f"{item}: ${prices[menu.index(item)]}")


def add_to_cart(item, cart, price):
    if find_menu(item, menu):
        cart.append(item)
        return f"Added! {item} for {price}"
    else:
        return f"{item} not found in the menu"


today_specials = specials()
show_menu(menu, prices, today_specials)

user_input = input("What would you like? ")
cart = user_input
print(f"You picked {cart}, that will be ${prices[menu.index(cart)]}")










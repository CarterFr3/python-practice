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
        print(f"Today's Special is {menu[0]}s for ${prices[0]}")
    elif random_special == "Fries":
        print(f"Today's Special is {menu[1]}s for ${prices[1]}")
    elif random_special == "Pizza":
        print(f"Today's Special is {menu[2]}s for ${prices[2]}")
    else:
        print(f"Today's Special is {menu[3]}s for ${prices[3]}")
    return random_special

def find_menu(item, menu):
    return item in menu if menu else None

def show_menu(menu, prices, today_specials):
    for item in menu:
        print(f"{item}: ${prices[menu.index(item)]}")

def add_to_cart(item, cart):
    if find_menu(item, menu):
        cart.append(item)
        return f"Added! {item}"
    else:
        return f"{item} not found in the menu"








today_specials = specials()
show_menu(menu, prices, today_specials)
print(add_to_cart("Pizza", cart))
print(add_to_cart("crackers", cart))
print(f"Your cart contains: {cart}")
# Needs a list of food items
menu_items = ["Pizza", "Burger", "Fries", "Pasta", "Coffee", "Soda"]

# find the food items in the list (Food item + Menu)
def find_item(name, menu):
    return name if name in menu else None
# select the item from the list
def select_item(name):
    return find_item(name, menu_items)

# Displaying Available menu items (look through menu and find the selection)
def show_available_items():
    print("Available Items Are: ")
    for menu in menu_items:
        print(menu)
    
# what you ordered and how many you ordered (selection + quantity)
def final_order_summary(name, quanity):
    if select_item(name):
        return f"You ordered {quanity} of the {name}"
    else:
        return "Meal not found"


print("Here is the order process with no assistance/ai")

show_available_items()

user_input = input("What would you like to order? ")
quanity_input = input("How much would you like? ")

final = final_order_summary(user_input, quanity_input)
print(final)


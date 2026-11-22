american_food = ["Burger", "Fries", "Chicken", "Soda"]
italian_food = ["Pasta", "Deli", "Pizza"]

def find_menu(name, menu): 
    return name in name if menu else None

def select_menu(name, food_type):
    if food_type == 'American':
        return find_menu(name, american_food)
    elif food_type == "Italian":
        return find_menu(name, italian_food)
    else:
        return None

def display_items(food_type):
    if food_type == "American":
        print("Available Items: ")
        for menu in american_food:
            print(menu)
    elif food_type == 'Italian':
        print("Available Items: ")
        for menu in italian_food:
            print(menu)
    else: 
        print("Food Item does not exist")

def summary_order(name, amount, food_type):
    order = select_menu(name, food_type)
    if order:
        return f"You have ordered {amount} {name}".lower()
    else: 
        return "Meal not found"

print("Thank you for using this ordering system! ")
type_input = input("What type do you want? ")
display_items(type_input)

user_input1 = input("What american food would you want? ")
user_input2 = input("What italian food would you want? ")

summary_order(user_input1, user_input2, type_input)
final = summary_order(user_input1, user_input2, type_input)
print(final)






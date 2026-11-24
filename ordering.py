
class Menu:
    def __init__(self, items):
        self.items = items
        self.orders = {}

    def display_menu(self):
        print("Available items are:")
        for item in self.items:
            print(item)

    def is_item_available(self, item_name):
        return item_name in self.items

class Order:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity


if __name__ == "__main__":
    menu_items = ["Pizza", "Burger", "Fries", "Pasta", "Coffee", "Soda"]
    menu = Menu(menu_items)

    print("Welcome to the Menu Ordering System!")
    menu.display_menu()

    user_input = input("What would you like to order? ")
    quantity_input = input("How much would you like? ")
    order = Order(user_input, quantity_input)

    if not menu.is_item_available(user_input):
        print("Sorry, that item is not available.")
    else:
        print(f"You ordered {order.quantity} of the {order.item_name}")

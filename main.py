from utils import menu_selector, safe_file_write


class Item:
    """creating an item class, so that I can attach its name, price and quantity by providing a list with those values,
    but quantity is automatically 0 if not supplied, since our file with store items only has name and price in it"""

    def __init__(self, input_list):
        self.name = input_list[0]
        self.price = int(input_list[1])
        if len(input_list) == 2:
            self.quantity = 0
        elif len(input_list) == 3:
            self.quantity = int(input_list[2])


class ShoppingCart:
    """creating a shopping cart class where we will put all our items that we buy and it contains the functions which
    manage cart contents"""
    cart_items = []   # list of Item objects

    def __init__(self):
        pass

    def add_item(self, item_to_add, amount):
        """method that adds item to the cart, with an input of Item object and the amount we want to add"""
        if item_to_add not in self.cart_items:
            self.cart_items.append(item_to_add)
            item_to_add.quantity = amount
            print(f"{item.name} added")
        else:
            decision = input(f"you already have {item_to_add.name}. do you still want more? (y/n)\n")
            decision = decision.lower()
            if decision == 'y' or decision == 'yes':
                item_to_add.quantity += amount
                print(f'ok, {item_to_add.name} added')
            elif decision == 'n' or decision == 'no':
                print("ok, I won't add more")
            else:
                print("i don't know what you mean, but I'll take that as no")

    def remove_item(self, item_to_remove, amount):
        """method that removes item objects from the cart, same concept as add_item"""
        if item_to_remove in self.cart_items:
            if amount > item_to_remove.quantity:
                print("you don't even have that many, i'll just remove all of that item")
                item_to_remove.quantity = 0
                del self.cart_items[self.cart_items.index(item_to_remove)]
            elif (item_to_remove.quantity - amount) == 0:
                item_to_remove.quantity = 0
                del self.cart_items[self.cart_items.index(item_to_remove)]
                print(f"ok, {item_to_remove.name} removed")
            else:
                item_to_remove.quantity -= amount
                print(f"ok, {item_to_remove.name} removed")
        else:
            print(f"{item_to_remove.name} is not in the cart")

    def check_cart(self):
        """method that prints item objects that are currently in the cart and calculates the total price"""
        print('this is your cart content:')
        total_price = 0
        products = []  # list of items
        for product in self.cart_items:
            print(f'{product.name}: {product.quantity}')
            products.append(product.name)
            total_price += product.price * product.quantity
        print(f'total price: {total_price}')

    def empty_cart(self):
        """method that deletes all items from the cart, by resetting the cart list"""
        self.cart_items = []
        print('ok, cart is now empty')


def print_store_items(items_list):
    """function that prints item objects in the store from the file supplied, takes a list of item objects"""
    print('these are the products that we have and their prices:')
    for store_item in items_list:
        print(f'{store_item.name} - {store_item.price}')


def get_products(user_cart):
    """function that makes a dictionary of items that were bought and how many, so that they can put in a file, takes
    a ShoppingCart object"""
    cart_products = {}
    for cart_product in user_cart.cart_items:
        cart_products[cart_product.name] = cart_product.quantity
    return cart_products


def read_file(file_name):
    """function that opens a file with items and makes a list from each row, and converts it to an Item object, requires
    the name of the file that needs to be read"""
    read_items = []
    items_file = open(file_name, 'r')
    item_line = items_file.readline().strip("\n")
    while not (item_line == "" or item_line is None):
        read_items.append(Item(item_line.split(";")))
        item_line = items_file.readline().strip("\n")
    items_file.close()
    return read_items


store_items = read_file('items.txt')  # making a list of item objects that are available in the store

# main menu
main_menu = ['start shopping', 'load my shopping list', 'leave the store']
shop_menu = ['show me the items that you have', 'add an item', 'remove an item',
             'see the cart', 'empty the cart', 'save shopping contents (as a file)', 'end shopping']
while True:
    main_decision = menu_selector(main_menu, 'welcome to the store\nwhat do you want to do?')  # menu fun from utils
    if main_decision == 1:
        print("okk let's start shopping")
        user_shopping_cart = ShoppingCart()
        while True:
            second_decision = menu_selector(shop_menu, 'what next?')
            if second_decision == 1:  # print items in the store
                print_store_items(store_items)
            if second_decision == 2:  # adds an item, if it exists in the store, and whatever amount the user wants
                user_item_name = input('what item do you want to buy?\n')
                user_item_name = user_item_name.lower()
                user_item = 0
                for item in store_items:
                    if item.name == user_item_name:
                        user_item = item
                        user_amount = int(input('how many?\n'))
                        if user_amount <= 0:
                            print("you can't add that amount")
                            continue
                        else:
                            user_shopping_cart.add_item(user_item, user_amount)
                if user_item == 0:
                    print("sorry, we don't have that")
            if second_decision == 3:  # removes the specified item if it's in the cart
                user_item_name = input('what item do you want to remove?\n')
                user_item = 0
                for item in user_shopping_cart.cart_items:
                    if item.name == user_item_name:
                        user_item = item
                        user_amount = int(input('how many?\n'))
                        user_shopping_cart.remove_item(user_item, user_amount)
                if user_item == 0:
                    print("that's not in your cart")
            if second_decision == 4:  # prints cart contents at the moment and their amount and price
                user_shopping_cart.check_cart()
            if second_decision == 5:  # clears the cart completely
                user_shopping_cart.empty_cart()
            if second_decision == 6:  # prints the cart contents to a txt file
                user_products = get_products(user_shopping_cart)
                if len(user_products) == 0:
                    file_decision = input("your cart is empty, do you still want to save it? y/n\n")
                    file_decision = file_decision.lower()
                    if file_decision == 'y' or file_decision == 'yes':
                        pass
                    elif file_decision == 'n' or file_decision == 'no':
                        print("ok, I won't save it")
                        continue
                    else:
                        print("i don't know what you mean, but I'll take that as a no")
                        continue
                user_file_name = input('how do you want to name your shopping .txt file?\n')
                if not user_file_name[-4:] == '.txt':
                    user_file_name = user_file_name + '.txt'
                user_file = safe_file_write(user_file_name)
                if user_file is None:
                    print('ok i will not save it')
                    continue
                user_file.write(str(user_products))
                print('ok, saved')
            if second_decision == 7:  # goes to the main menu
                break
    if main_decision == 2:  # prints shopping list file contents, with names and quantities of items
        shopping_list = read_file('shopping_list.txt')
        for shopping_item in shopping_list:
            print(f'{shopping_item.name}: {shopping_item.quantity}')
    if main_decision == 3:  # exits the program completely
        print('bye~~')
        break

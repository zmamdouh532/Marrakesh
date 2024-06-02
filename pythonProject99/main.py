


class ItemToPurchase:
    # The given code is an implementation of an online shopping cart. It consists of a class ItemToPurchase which has three attributes - item_name, item_price, and item_quantity, and a method print_item_cost().
    # The constructor of the ItemToPurchase class initializes the attributes to default values of "none", 0, and 0. The print_item_cost()
    # ItemToPurchase class are created using the default constructor. The user is prompted to enter the details of the items - item name, price, and quantity - which are then assigned to the corresponding attributes of the objects.
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantit, y *self.item_price}")


item1 = ItemToPurchase()
print("Item 1")
item1.item_name = input("Enter the item name: ")
item1.item_price = int(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

item2 = ItemToPurchase()
print("\nItem 2")
item2.item_name = input("Enter the item name: ")
item2.item_price = int(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

# The total cost of the items is calculated by multiplying the price and quantity of each item and adding them together. The total cost and the details of each item are then printed using the print_item_cost() method.

total_cost = item1.item_quantity*item1.item_price + item2.item_quantity*item2.item_price

print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name1='none', current_date1='January 1, 2016'):
        self.customer_name = customer_name1
        self.current_date = current_date1
        self.cart_items = []

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, itemName):
        tremove_item = False

        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                tremove_item = True
                break

        if not tremove_item:
            print('Item not found in the cart. Nothing removed')

    def modify_item(self, itemToPurchase):
        modify_item1 = False

        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemToPurchase.item_name:
                modify_item1 = True

                if (
                    itemToPurchase.item_price != 0
                    or itemToPurchase.item_quantity != 0
                    or itemToPurchase.item_description != 'none'
                ):
                    if itemToPurchase.item_price != 0:
                        self.cart_items[i].item_price = itemToPurchase.item_price
                    if itemToPurchase.item_quantity != 0:
                        self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                    if itemToPurchase.item_description != 'none':
                        self.cart_items[i].item_description = itemToPurchase.item_description

                break

        if not modify_item1:
            print('Item not found in the cart. Nothing modified')

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost1 = 0
        for item in self.cart_items:
            cost = item.item_quantity * item.item_price
            total_cost1 += cost
        return total_cost1

    def print_total(self):
        total_cost1 = self.get_cost_of_cart()
        if total_cost1 == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: %d\n' % self.get_num_items_in_cart())
            for item in self.cart_items:
                item.print_item_cost()

            print('\nTotal: $%d' % total_cost1)

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()

def print_menu(newCart1):
    customer_Cart = newCart1
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from the cart\n'
            'c - Change item quantity\n'
            "i - Output item's descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n')

    command = ''
    while command != 'q':
        print(menu)
        command = input('Choose an option:')
        while (
            command != 'a'
            and command != 'o'
            and command != 'i'
            and command != 'q'
            and command != 'r'
            and command != 'c'
        ):
            command = input('Choose an option:\n')

        if command == 'a':
            print("\nADD ITEM TO CART")
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_Cart.add_item(itemtoPurchase)

        elif command == 'o':
            print('\nOUTPUT SHOPPING CART')
            customer_Cart.print_total()
        elif command == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            customer_Cart.print_descriptions()
        elif command == 'r':
            print('REMOVE ITEM FROM CART')
            itemName = input('Enter the name of the item to remove :\n')
            customer_Cart.remove_item(itemName)
        elif command == 'c':
            print('\nCHANGE ITEM QUANTITY')
            itemName = input('Enter the name of the item :\n')
            qty = int(input('Enter the new quantity :\n'))
            itemToPurchase = ItemToPurchase(itemName, 0, qty)
            customer_Cart.modify_item(itemToPurchase)

if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name: %s" % customer_name)
    print("Today's date: %s" % current_date)
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)
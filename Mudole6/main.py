from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart



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

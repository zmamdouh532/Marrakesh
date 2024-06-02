class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        # Initialize attributes for the item
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # Print the cost of the item
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Initialize the shopping cart with customer name, current date, and an empty list for cart items
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        # Add an item to the shopping cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Remove an item from the shopping cart by its name
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, new_item):
        # Modify an item's quantity in the cart
        for item in self.cart_items:
            if item.item_name == new_item.item_name:
                item.item_quantity = new_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Get the total quantity of items in the cart
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        # Calculate the total cost of items in the cart
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        # Print the shopping cart's contents and total cost
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        total_cost = self.get_cost_of_cart()
        for item in self.cart_items:
            item.print_item_cost()
        print("Total:", f"${total_cost}")

    def print_descriptions(self):
        # Print descriptions of items in the cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    while True:
        # Display the main menu and handle user input
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            # Add an item to the cart
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
        elif choice == 'r':
            # Remove an item from the cart
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)
        elif choice == 'c':
            # Change the quantity of an item in the cart
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            new_item = ItemToPurchase(item_name, 0, new_quantity)
            cart.modify_item(new_item)
        elif choice == 'i':
            # Output item descriptions
            cart.print_descriptions()
        elif choice == 'o':
            # Output the shopping cart
            cart.print_total()
        elif choice == 'q':
            # Quit the program
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    # Get customer's name and today's date
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Create a shopping cart and start the menu
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


class Additional:
    pass
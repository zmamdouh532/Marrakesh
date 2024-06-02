
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        # Initialize attributes for the item
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description


def print_item_cost(self):
    print(f'{self.item_name} {self.item_quantity} @ {self.item_price * self.item_quantity}')

item1 = ItemToPurchase()
item1.item_name = input('Enter the item name:')
item1.item_price = float(input('Enter the item price:'))
item1.item_quantity = int(input('Enter the item quantity:'))

item2 = ItemToPurchase()
item2.item_name = input('Enter the item name:')
item2.item_price = float(input('Enter the item price:'))
item2.item_quantity = int(input('Enter the item quantity:'))

total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
print('Total: $', total_cost)

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Initialize the shopping cart with customer name, current date, and an empty list for cart items
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []


def add_item(self, item):
    self.cart_items.append(item)


def remove_item(self, item_name):
    for item in self.cart_items:
      if item.item_name == item_name:
         self.cart_items.remove(item)
         break
      else:
           print('Item not found in cart. Nothing removed.')

def modify_item(self, item):
    for i in self.cart_items:
        if i.item_name == item.item_name:
           i.item_price = item.item_price
           i.item_quantity = item.item_quantity
           break
        else:
            print('Item not found in cart. Nothing modified.')

def get_num_items_in_cart(self):
  return sum(item.item_quantity for item in self.cart_items)
def get_cost_of_cart(self):
  return sum(item.item_price * item.item_quantity for item in self.cart_items)

def print_total(self):
    if len(self.cart_items) == 0:
     print('SHOPPING CART IS EMPTY')
    else:
     print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
     print('Number of Items:', self.get_num_items_in_cart())
    for item in self.cart_items:
        item.print_item_cost()
    print('Total: $', self.get_cost_of_cart())


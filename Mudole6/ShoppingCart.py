class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
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
        tmodify_item = False

        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemToPurchase.item_name:
                tmodify_item = True

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

        if not tmodify_item:
            print('Item not found in the cart. Nothing modified')

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            cost = item.item_quantity * item.item_price
            total_cost += cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: %d\n' % self.get_num_items_in_cart())
            for item in self.cart_items:
                item.print_item_cost()

            print('\nTotal: $%d' % (total_cost))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()




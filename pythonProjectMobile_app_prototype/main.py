# Class representing the Shopping List App
class ShoppingListApp:
    def __init__(self):
               # Initialize an empty shopping list
               self.shopping_list = []
    def add_item(self, item):
              # Add an item to the shopping list
              self.shopping_list.append(item)

    def remove_item(self, item):
            # Remove an item from the shopping list
            if item in self.shopping_list:
                  self.shopping_list.remove(item)

    def view_shopping_list(self):
            # Display the current shopping list
            for item in self.shopping_list:
                  print(item)

# Instantiate the ShoppingListApp
shopping_app = ShoppingListApp()

# Add items to the shopping list
shopping_app.add_item("Milk")
shopping_app.add_item("Bread")

# Remove an item from the shopping list
shopping_app.remove_item("Bread")

# View the current shopping list
shopping_app.view_shopping_list()

# List of Tools Used for Development
tools_used = ["UML (Unified Modeling Language) for architectural design",
                              "Paper and pen for paper prototype sketches",
                              "Python for scripting"]

# Print pseudocode and list of tools
print("Pseudocode for Preliminary Architectural Design:")
print("------------------------------------------------")
print("1. Create a class for the Shopping List App.")
print("2. Include methods for adding, removing, and viewing items in the shopping list.")
print("3. Instantiate the app, add and remove items, and view the current list.")

print("\nList of Tools Used for Development:")
print("------------------------------------")
for tool in tools_used:
       print(tool)

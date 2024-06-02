"""
To create a preliminary architectural design for a mobile app that
lets users save a shopping list on their devices,
I would first identify the key components and functionalities of the app.
This would include user interface, data storage, and the logic for adding, removing,
 and editing items in the shopping list.
I would use a UML tool like UMLet to create diagrams representing
the architecture of the app. The diagrams would include a use case diagram
to show the interactions between the user and the system,
a class diagram to represent the data structure, and a sequence diagram
to illustrate the flow of operations.
For the paper prototype, I would sketch the key screens of the app,
such as the main screen showing the shopping list,
the screen for adding a new item, and the screen for editing an existing item.
To write a Python script that prints out the names and number
of pages in the prototype and the sequence or flow of the pages,
I would first create a list of dictionaries, where each dictionary represents
a page in the prototype. Each dictionary would contain the name of the page and
the number of pages. Then, I would iterate over the list and print out the information.
Here is an example of how the Python script might look:
"""



pages \
     = [
    {"name": "Main Screen", "number": 1},
    {"name": "Add Item Screen", "number": 2},
    {"name": "Edit Item Screen", "number": 3},
]

for page in pages:
    print(f"Page Name: {page['name']}, Number of Pages: {page['number']}")

print("Sequence of Pages: ", " -> ".join([page['name'] for page in pages]))


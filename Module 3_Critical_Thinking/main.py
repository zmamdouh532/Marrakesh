"""
Mamdouh Zayed

A preliminary architectural design for a mobile app 
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
    {"name": "Remove Item Screen", "number" : 3},
    {"name": "Edit Item Screen", "number": 4},
]

for page in pages:
    print(f"Page Name: {page['name']}, Number of Pages: {page['number']}")

print("Sequence of Pages: ", " -> ".join([page['name'] for page in pages]))


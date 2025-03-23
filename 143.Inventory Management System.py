'''
Project Description
    Build a command-line app that allows a small business to manage their inventory. 
    The app will let users:
        add new item
        update stock
        view all items
        search for specific items by name
    This project is perfect for practicing CRUD (Create, Read, Update, Delete) operations using dictionaries.

Learning Benefits
    You will practice CRUD operations, dictionary manipulation, and handling user input while building a tool that models real-world applications.
'''

class inventory:
    def __init__(self):
        self.inv={}

    def add(self):
        name=input("enter item name: ").strip()
        quantity=int(input("enter quantity: "))
        price=float(input("enter price: "))
        self.inv[name]=[quantity,price]
        print("item added successfully!")

    def update(self):
        name=input("enter item name to update: ").strip()
        quantity=int(input("enter new quantity: "))
        self.inv[name][0]=quantity
        print("stock updated successfully!")
    def view(self):
        i=1
        for j in list(self.inv.keys()):
            print(f"{i}. {j} - quantity: {self.inv[j][0]}, price: ${self.inv[j][1]}")
            i+=1
    def search(self):
        name=input("enter item name to search: ").strip()
        for i in list(self.inv.keys()):
            if i==name:
                print(f"found: {name} - quantity : {self.inv[name][0]}, price: ${self.inv[name][1]}")
                return
        print("item not found")

inven=inventory()
option=0

while option!=5:
    print("\nwelcome to the inventory management system!\n")
    print("1. add new item\n2. update stock\n3. view inventory\n4. search for an item\n5. exit\n")
    option=int(input("choose an option: "))
    if option==1:
        inven.add()
    elif option==2:
        inven.update()
    elif option==3:
        inven.view()
    elif option==4:
        inven.search()
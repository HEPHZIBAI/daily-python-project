'''
Project Description
    Create a command line program that simulates a basic billing system for a supermarket. 
    The user can input items purchased (e.g., butter, eggs, etc), their prices, and quantities. 
    The app will calculate the total bill, apply any applicable discounts, and display an itemized bill summary. 
    This project focuses on loops, dictionaries, and arithmetic calculations.

Learning Benefits
    You will practice working with loops, dictionaries, and arithmetic calculations while simulating a real-world application. 
    This project helps improve your problem-solving skills and teaches you how to handle user input and display formatted output.
'''

print("welcome to the supermarket billing system:")
number=int(input("enter the number of items: "))
items={}

for i in range(number):
    print(f"item {i+1}:")
    name=input("name: ")
    price=float(input("price per unit: "))
    quantity=int(input("quantity: "))
    items[name]=[price,quantity]

print("---bill summary---")
t=0

for i in list(items.keys()):
    print(f"{i} : {items[i][1]} X ${items[i][0]} = ${items[i][1]*items[i][0]}")
    t+=items[i][1]*items[i][0]

print("subtotal: $",t)
print("discount: $0.00")
print("sales Tax (5%): $0.53")
print("total: $",t+0.53)
print("\nthank you for shopping with us!")
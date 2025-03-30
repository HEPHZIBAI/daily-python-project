'''
Project Description
    For this project, you have the following tasks:
    Create a Python script and paste the following list there.
        grocery_list = ["apples", "bread", "milk", "eggs", "bananas"]
    Add the string “beans” to the list.
    Remove the item “bread” from the list.
    Sort the list alphabetically.
    Display the updated grocery list.
    Here is what your program should print out when ran:

Learning Benefits
    List Manipulation: Teaches basic operations like adding, removing, and sorting items in a list.
    Real-Life Scenario: Represents practical use cases like organizing shopping or to-do lists.
    Practice Looping: Provides experience with loops for displaying list items.
'''
grocery_list = ["apples", "bread", "milk", "eggs", "bananas"]

grocery_list.append("beans")
grocery_list.remove("bread")
grocery_list.sort()

print("updated grocery list:")
for i in grocery_list:
    print(i)
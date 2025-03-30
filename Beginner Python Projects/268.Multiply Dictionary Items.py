'''
Project Description
    This project starts with a pre-defined dictionary representing a grocery list with quantities:

    grocery_list = {
        "apples": 5,
        "bananas": 2,
        "milk": 1,
        "bread": 1
        }

    You task is to add some code that updates all the values of the dictionary by multiplying them by 10. 
    Then, print out the updated dictionary.

Expected Output
    The program should display the updated dictionary in the command line:

Learning Benefits
    Dictionary Manipulation:Practice accessing and updating dictionary values efficiently.
    Iteration Skills:Learn how to iterate over keys in a dictionary to apply changes.
    Mathematical Operations:Combine looping with basic arithmetic to modify data dynamically.
'''

grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}

for i in list(grocery_list.keys()):
    grocery_list[i]*=10

print(grocery_list)
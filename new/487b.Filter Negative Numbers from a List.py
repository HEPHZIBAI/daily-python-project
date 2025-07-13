'''
Project Description
    Your task for today is to write a Python program that takes a list of numbers and removes all the negative ones. 
    The goal is to keep only numbers that are greater than or equal to zero.
    This is a great exercise in list filtering, which is something you’ll often need in real-world projects like:

    Cleaning data for analysis
    Preparing inputs for machine learning
    Validating form entries or user input

You’ll start with a predefined list of integers — some positive, some negative, and maybe even zero. 
Store that list in a variable like so:
    numbers = [3, -1, 7, -5, 0, 8, -2]
Your program should create a new list that includes only the non-negative numbers and then print it.

Expected Output
    If the list is:
        [3, -1, 7, -5, 0, 8, -2]
    Then your program should print:
'''

a=[3, -1, 7, -5, 0, 8, -2]
b=[]

for i in a:
    if i>=0:
        b.append(i)

print(b)
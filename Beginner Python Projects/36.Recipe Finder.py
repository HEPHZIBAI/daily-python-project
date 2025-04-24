'''
Project Objective
    Create a Python program that takes a list of ingredients from the user and displays recipes that can be made using those ingredients.

Learning Benefits
    In this project, you will practice file handling and JSON data parsing while searching for recipes based on user-provided ingredients. 
    This project will reinforce your understanding of conditional logic and data structures in Python.

How the Program Works
    The user is prompted to enter a list of ingredients they at home:
    Once the user enters the ingredients, they will get all the recipes that can be cooked using those ingredients. For example, since the user had bread, salt, and oil, the oil bruschetta recipe showed up since it was the recipe in the JSON file that had can be made with the ingredients that the user had.
    You can use this sample JSON file containing 21 recipes.

Prerequisites
    Required Libraries: json
    Required Files: Download the JSON file given in the link above.
'''

ing=input("enter a list of ingredients , separated by commas: ").split(',')
print("here are some recipes you can make:")
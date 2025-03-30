'''
Project Description
    Create a program that reads a list of motivational quotes from a text file and selects one to display every Monday (or any day the user runs the program). 
    It uses Python's date handling to check the current day and ensures you’re greeted with a new quote each time you run it.

Expected Output
    A) Scenario 1: If Monday
        The program checks what day it is. 
        If it is Monday it displays the another text as shown above and picks a quote from the quotes.txt file.
    B) Scenario 2: If not Monday
        If it is not Monday, the program displays some other text as shown below:

Learning Benefits
    File Handling: 
        You will practice reading data from a file, a foundational skill for working with external resources such as databases, logs, or configuration files.
    Randomization: 
        You will practice using the random module to generate unpredictable results, which is common in applications like games, recommendations, and creative tools.
    String Processing: 
        You will practice parsing and manipulating strings, such as slicing, stripping whitespace, and formatting text for better readability.
    Control Flow: 
        You will practice logical structures like if-else to make decisions based on user input, a core aspect of interactive programs.
    Output Formatting: 
        You will practice creating user-friendly console outputs, a valuable skill for making your programs engaging and easy to use.

Prerequisites
    Required Libraries: random, datetime
    Required Files: Download the text file in this link and place it in the same directory as your Python script.
'''

import datetime,random

current=(datetime.datetime.now().strftime("%A")).lower()

if current=="monday":
    with open("258.Motivational Quote of the Day.txt", "r") as file:
        quotes = file.readlines()
    print("it's monday! time for some motivation!")
    print(random.choice(quotes))
else:
    print(f"today is {current}!")
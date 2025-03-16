'''
Project Description
    Build a habit tracker desktop app where users can add, complete, and monitor daily habits (e.g., drinking water, exercising, reading). 
    The app will display the streak (e.g., 2 days) and store data locally in a JSON file.

Expected Output
    The program allows the user to add habits (e.g., “Be positive”):
    The habit is added to the stack. 
    The user can also press the “Complete” button whenever they complete a habit:
    And here is what the JSON data looks like for the above examples. 
    The data are added by the program automatically.

    {     "Meditate": {         "streak": 1,         "last_completed": "2025-01-27"     },     "Be positive": {         "streak": 0,         "last_completed": ""     } }

Prerequisites
    Required Libraries: tkinter, json, datetime

'''


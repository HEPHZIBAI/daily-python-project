'''
Project Description
    This program asks the user to enter their birth year and the current year. 
    It then calculates and displays the user's age.

Project Skills Needed
    This project covers the following concepts. Click any link to learn more about them if you're unfamiliar with them.
    input() function | print() function | strings

How the Project Works
    (1) The program starts by asking the user to enter their birth year. 
    (2) Next, it asks the user to enter the current year. 
    (3) The program calculates the user's age by subtracting the birth year from the current year. 
    (4) Finally, it displays a message in the terminal that includes the calculated age.
'''

birth=int(input("enter your birth year: "))
current=int(input("enter the current year: "))

print(f"you are {current-birth} years old.")
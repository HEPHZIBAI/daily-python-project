'''
Project Description
    Create a program that lets the user submit three numbers and the program calculates the maximum number.

How the Project Works
    (1) The program prompts the user to enter a number in the terminal:
    (2) The user types in a number (e.g., 7) and presses Enter. The program prompts the user to enter two more numbers:
    After the user enters the third number, the program displays a message with the maximum number out of the three numbers.
'''

f=int(input("enter the first number: "))
s=int(input("enter the second number: "))
t=int(input("enter the third number: "))

print("the largest of the three numbers is: ",max(f,s,t))
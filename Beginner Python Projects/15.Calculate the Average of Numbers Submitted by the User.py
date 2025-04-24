'''
Project Description
    Create a program that lets the user submit three numbers and returns the average of those numbers.

How the Project Works
    (1) The program prompts the user to enter a first number in the terminal:
    (2) Once the user submits a number (e.g., 4), the program asks the user to submit two more numbers:
    After submitting the third number, the program prints out a message containing the average of all three numbers. 
    The average should be in two decimal points format (e.g., 3.33).
'''

f=int(input("enter the first number: "))
s=int(input("enter the second number: "))
t=int(input("enter the third number: "))

print("the average of the three numbers is: ",(f+s+t)//3)
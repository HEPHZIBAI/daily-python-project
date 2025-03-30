'''
Project Description
    This program asks the user to input a number and checks whether it is positive, negative, or zero.

How the Project Works
    The program prompts the user to submit a number in the console. 
    Once the user submits a number (e.g., -11), the program checks the sign of the number (e.g., negative, zero, or positive) and returns a message accordingly.

    If the number is positive:
    If the number is zero:
'''
number=int(input("enter a number: "))
if number>0:
    print("the number is positive")
elif number==0:
    print("the number is zero")
else:
    print("the number is negative")
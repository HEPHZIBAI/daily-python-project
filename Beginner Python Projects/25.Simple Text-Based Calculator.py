'''
Project Description
    Build a program that the user to input two numbers and an operation (addition, subtraction, multiplication, or division). 
    It performs the operation on the two numbers and displays the result.

How the Project Works
    The program lets the user input two numbers (e.g., 4 and 8). 
    Then, the program lets the user input an operation (e.g., * for multiplication). 
    Finally, the program displays the result of the operation.
'''

first=float(input("enter the first number: "))
second=float(input("enter the second number: "))
operation=input("enter operation (+,-,*,/): ").strip()
print("the result is: ",end="")

if operation=='+':
    print(first+second)
elif operation=='-':
    print(first-second)
elif operation=='*':
    print(first*second)
elif operation=='/':
    print(first//second)
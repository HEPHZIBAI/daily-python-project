'''
Project Description
    Create a program that checks if a number is even or odd.

How the Project Works
    (1) The program prompts the user to enter a number in the terminal:
    (2) The user types in a number (e.g., 3) and presses Enter. 
    The program checks the number and prints out either “The number X is odd.” or “The number X is even.” 
    depending on the number:
'''

num=int(input("enter a number: "))

if num%2==0:
    print(f"the number {num} is even")
else:
    print(f"the number {num} is odd")
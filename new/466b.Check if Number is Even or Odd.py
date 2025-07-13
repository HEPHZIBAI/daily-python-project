'''
Project Overview 💡
    In this beginner-friendly project, you’ll write a Python program that checks whether a number entered by the user is even or odd. 
    This is a great way to practice input handling, number conversion, and conditional logic.

Task:
    Write a Python program that:
    Asks the user to input a number
    Converts it from string to integer
    Uses the modulus operator to determine if it's even or odd
    Prints the result accordingly

Expected Output:
    (1) The program prompts the user to enter a number in the terminal:
    (2) The user types in a number (e.g., 3) and presses Enter. The program checks the number and prints out either “The number X is odd.” or “The number X is even.” depending on the number:

Comparison
    The original version is concise and good for clean input.
    The alternative version is more user-proof by handling errors gracefully.
'''

num=int(input("enter a number: "))

if num%2==0:
    print(f"the number {num} is even")
else:
    print(f"the number {num} is odd")
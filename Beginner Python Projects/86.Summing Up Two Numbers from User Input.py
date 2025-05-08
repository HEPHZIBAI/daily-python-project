'''
Project Overview 💡
    In this project, you’ll learn how to take user input, convert it into numbers, and calculate their sum. 
    This is an essential skill for handling user interactions in Python programs.

Task:
    Write a Python script that asks the user for two numbers, converts them to integers, sums them up, and prints the result.

Expected Output:
    The program should ask for two numbers and display their sum. 
    In the following example, the user entered 12 and then 4. 
    The program prints out the output in the last line.

Extra Challenge 🚀
    Modify the script to handle cases where the user enters non-numeric values. 
    Use a try-except block to catch errors and ask the user to enter numbers again.
'''
def add():
    try:
        a=int(input("enter the first number: "))
        b=int(input("enter the second number: "))
        print("the sum of the two numbers is:",a+b)
    except:
        print("invalid input! please enter numbers only.")
        add()

add()
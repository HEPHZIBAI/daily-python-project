'''
Project Overview 💡
    In this project, you’ll practice basic string manipulations in Python. 
    You’ll ask the user for their full name, then perform various operations like converting to uppercase/lowercase, removing spaces, counting characters, and reversing the name.

Task:
    Write a Python program that:
    Accepts a user's full name as input
    Prints the name in uppercase and lowercase
    Removes spaces and counts the characters
    Reverses the name

Expected Output: 
    Here is how the program would work. The program asks the user to enter their name (e.g., user enters “John Smith”) and then prints out the output.


Comparison
    The original version does each operation directly in sequence.
    The alternative version groups logic inside a function — better for reuse and organization. 
    Using functions is better for more complex programs. 
    For our program, the original version is optimal.
'''

name=input("please enter your full name: ").strip()
print("your name in uppercase: ",name.upper())
print("your name in lowercase: ",name.lower())
k=name.replace(' ','')
print("total number of characters (excluding spaces): ",len(k))
print("your name reversed: ",name[::-1])
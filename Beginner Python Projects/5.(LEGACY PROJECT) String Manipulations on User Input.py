'''
Project Description
    In this project, you will create a simple program that asks the user to enter their full name, and the program will perform several operations to the user entry as described in the “How Project Works” section further below.

How the Project Works
    (1) First your program prompts the user to enter their name (first and last) in the terminal 
    (2) The user types in their name. 
    (3) Then, your program displays the user’s name in uppercase and then in lowercase. 
    (4) Next, the total number of characters is displayed. 
    (5) Lastly, the program reverses the user’s name and displays it.

Project Skills Needed
    This project covers the following concepts. Click any link to learn more about them if you're unfamiliar.
    input() function | print() function | strings | len() function
'''

name=input("please enter your full name: ").strip()
print("your name in uppercase: ",name.upper())
print("your name in lowercase: ",name.lower())
k=name.replace(' ','')
print("total number of characters (excluding spaces): ",len(k))
print("your name reversed: ",name[::-1])
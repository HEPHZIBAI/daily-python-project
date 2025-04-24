'''
Project Overview 💡
    In this project, you’ll build a basic contact list manager using Python. 
    The app allows users to enter names and phone numbers and saves the list to a text file. 
    This project helps reinforce concepts like loops, lists, string formatting, and file I/O.

Task:
    Write a Python program that:
    Prompts the user to input contact names and phone numbers
    Stores each contact as a name-number pair
    Saves the list to a text file when the user finishes entering contacts

Expected Output: 
    The program prompts the user to enter names and phone numbers through the terminal:
    If the user enters “done” the program ends and saves the data in a contacts.txt file which looks like the following:
    Give it a shot! Scroll down when you're ready for the step-by-step guide.

Comparison
    The original version uses a list of formatted strings, which is simple and effective for small projects.
    The alternative version uses a dictionary, which is more flexible if you plan to add features like searching or deleting contacts.
'''

while True:
    name=input("enter contact name (or type 'done' to finish): ").strip()
    if name=='done':
        break
    phone=input(f"enter phone number for {name}: ").strip()
    with open("./Beginner Python Projects/93.Simple Contact List Manager.txt",'a') as f:
        f.write(name+":"+phone)

print("contacts saved.")
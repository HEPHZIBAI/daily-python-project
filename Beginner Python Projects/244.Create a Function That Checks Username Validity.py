'''
Project Description
    This program creates a function that checks whether a username is valid based on some simple rules. 
    The function will take a username as input and return whether it is valid or not. 
    The rules for a valid username are:
        The username must be between 5 and 15 characters.
        It must contain only alphanumeric characters (letters and numbers).
        It must start with a letter.

How the Project Works
    Define a function called check_username_validity that takes a string (the username) as an argument.
    Inside the function, write conditions to check:
        If the length of the username is between 5 and 15 characters.
        If the username contains only alphanumeric characters using Python's built-in isalnum() method.
        If the first character of the username is a letter using isalpha().
        If all conditions are met, return "Valid username." Otherwise, return a message indicating why the username is invalid.
    Here is how the program behaves when it is called with a valid username:
    Here is how the program behaves when it is called with a non-valid username:
'''

def check_username_validity(username):
    condition=[]

    if not(len(username)>=5 and len(username)<=15):
        condition.append("length must be 5-15")
    
    if not username.isalnum():
        condition.append("user name shoud have only alphanumeric characters")
    
    if not username[0].isalpha():
        condition.append("first character should be character")

    return condition

username=input("enter the username: ")
condition=check_username_validity(username)

if len(condition)==0:
    print("valid username")
else:
    print("invalid username")
    for i in condition:
        print(i)
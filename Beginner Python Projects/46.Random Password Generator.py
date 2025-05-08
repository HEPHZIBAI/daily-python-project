'''
Project Description
    Create a command-line app that generates secure random passwords based on user preferences. 
    The user can specify the password length and 
    whether to include uppercase letters, numbers, and special characters. 
    This project focuses on randomness, string operations, and user input validation.

Expected Output
    The program starts by asking the user a few questions, such as the desired password length, and if there have to be any uppercase letters, numbers, or special characters in the password. 
    Depending on the user's answers, the program generates a password and prints it out, as shown in the screenshot above.

Learning Benefits
    You will practice working with randomness, string operations, and user input validation. This project helps you understand how to build customizable tools for practical use.

Prerequisites
    Required Libraries: random, string
'''
import random
import string

print("welcome to the password generator!")
lenght=int(input("enter desired password length (minimum 6): "))
upper=input("include uppercase letters? (yes/no): ").strip()
lower=input("include lowercase letters? (yes/no): ").strip()
number=input("include numbers? (yes/no): ").strip()
special=input("include specal characters? (yes/no): ").strip()

characters = ""

if upper=='yes':
    characters += string.ascii_uppercase
if lower=='yes':
    characters += string.ascii_lowercase
if special=='yes':
    characters += string.punctuation
if number=='yes':
     characters += string.digits

password=""

for i in range(lenght):
    password+=random.choice(characters)

print("generated password :" ,password)
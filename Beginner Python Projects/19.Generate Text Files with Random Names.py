'''
Project Description
    Your task for today is to create a Python program which generates a new text file every time you run it.

How the Project Works
    When you run the program, it should generate a new text file. 
    The program assigns a random name of 10 characters to the text file and also writes that random text inside the text file as content.
    Here is an example of the file generated when the program is executed:
    Any time the program is executed, a new file with a different

Prerequisites
    Required Libraries: string, random
    Required Files: No files are required.
    IDE: You can use any IDE on your computer to code the project.

Danger Zone
    Get help by obtaining the code that generates a random string below:
'''
import string
import random

name=''.join(random.choices(string.ascii_letters + string.digits, k=10))
word=input("enter the name : ").strip()

with open("./Beginner Python Projects/19.Generate Text Files with Random Names/"+word+".txt",'w') as f:
    f.write(name)

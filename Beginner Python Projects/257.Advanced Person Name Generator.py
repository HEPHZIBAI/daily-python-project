'''
Project Description
    In a previous beginner project, we created a program that picks a random name out of a long list of names in a text file. 
    Today, your task is to create a similar but more complex program.
    (1) The program starts by showing the user a menu.
    (2) The user enters a number (e.g., 2 to add a new name to the text file) and then proceeds with the instructions (e.g., adding a name such as Wimbly). 
    (3) The program adds that new name to the names.txt file and then shows the menu again. 
    In addition to adding new names, the user can also display the total number of names, and select a random name from the text file.

Learning Benefits
    his project provides a more comprehensive look at working with file handling in Python. 
    By implementing a menu and multiple functionalities, students gain experience with designing user-friendly command-line interfaces, modifying files dynamically, and working with lists and loops.

Prerequisites
    Required Libraries: random
    Required Files: Download the text file in this link.
'''
import random

option=0

while option!=4:
    print("please select an option:")
    print("\n1. show the total number of names\n2. add a new name\n3. select a random name\n4. exit\n")
    option=int(input("enter your choice (1-4): "))

    if option==1:
        readfile=open("257.Advanced Person Name Generator.txt",'r')
        names=readfile.readlines()
        print("total number of names: ",len(names))
        readfile.close()
    elif option==2:
        newname=input("enter the new name to add: ").strip()
        print(newname," has been added to the file.")
        writefile=open("257.Advanced Person Name Generator.txt",'a')
        writefile.write(newname+"\n")
        writefile.close()
    elif option==3:
        readfile=open("257.Advanced Person Name Generator.txt",'r')
        names=readfile.readlines()
        print(random.choice(names))
        readfile.close()
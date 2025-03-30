'''
Project Description
    Create a program that reads a list of names from a text file, randomly picks one, and displays it. 
    It's perfect for practicing file handling and working with lists in Python.
    Download the text file from this link. 
    The text file contains 4945 person names. 
    Here is a snapshot of the text file:

Learning Benefits
    This project is about reading text from files, processing text data, and applying the random.choice() function on lists, all while building a program that’s both useful and easy to expand.

Prerequisites
    Required Libraries: random
    Required Files: Download the text file in this link.
'''
import random

readfile=open("256.Generate Random Person Name.txt",'r')
names=readfile.readlines()
print("randomly selected name: ",random.choice(names))
readfile.close()
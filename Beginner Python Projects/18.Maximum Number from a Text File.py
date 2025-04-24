'''
Project Description
    In a previous project, we created a program that prompted the user to submit three numbers in the terminal and then the program returned the maximum number. For this project, instead of getting the numbers from the terminal, we will get them from a text file.

Before Coding the Project
    Download the text file in this link and place the text file in the same directory with your Python script. 
    The text file contains some numbers:

How the Project Works
    The program reads the numbers.txt file, stores the numbers in a list or similar, and returns the maximum number. 
    The output should be similar to the following:
'''
arr=[]

with open("./Beginner Python Projects/18.Maximum Number from a Text File.txt",'r') as f:
    for i in f.readlines():
        arr.append(int(i))

print("the maximum number in the file is: ",max(arr))
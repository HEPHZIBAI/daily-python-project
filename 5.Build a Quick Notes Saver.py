'''
Project Description
    Create a simple program that allows users to quickly save notes to a text file and read them later.

How the Program Works
    Anytime the user runs the program, it lets the user type in a note:

Here is another example:
    All notes are saved in a notes.txt file, one in each line:

How This Project Matters in the Real-World
    This project introduces file handling, a fundamental skill in software development. 
    In real-world applications, text files are commonly used to store logs, configuration settings, and user data. 
    For example, a journaling app or a simple logging system might write entries to a text file just like this program does. 
    Understanding how to append data to a file is a useful stepping stone to working with databases and cloud storage solutions.

'''
f=open("5.Build a Quick Notes Saver.txt",'a')
print("if you want to stop type stop(without any character or space)")
note=input("write a note : ")
while note!="stop":
    f.write(note+"\n")
    note=input()
print("note saved!")
f=open("5.Build a Quick Notes Saver.txt",'r')
print(f.read())
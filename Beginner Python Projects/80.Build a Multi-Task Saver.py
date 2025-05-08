'''
Project Description
    Create a program that allows the user to input multiple tasks, save them to a text file, and then display all saved tasks. 
    This program is a more advanced version of yesterday’s project where we simply recorded notes, but didn’t display them in the terminal.

How the Program Works
    When the user runs the program, it lets the user type in a new task, and it also displays all the existing tasks:
    Here is a second execution of the program:
    As you can see, this time, there are two tasks recorded and displayed in the terminal.
    The program should save the tasks in a tasks.txt file. Here is how the tasks.txt file looks at this point:

How This Project Matters in the Real-World
    In real-world applications, users often need to add multiple entries to a file and retrieve them later. 
    This project helps you practice working with multiple lines of data, appending new information, and reading from files—skills that are essential when managing logs, user inputs, or even data backups in production systems.

'''
f=open("./Biginner Python Projects/80.Build a Multi-Task Saver.txt",'r')
k=f.readlines()
l=len(k)+1
f=open("./Biginner Python Projects/80.Build a Multi-Task Saver.txt",'a')
print("if you want to sto.p type \'stop\'")
task=input("enter a task:")
while task!='stop':
    f.write(str(l)+'.'+task+'\n')
    task=input("enter a task:")
    l+=1

print("all saved task :")
f=open("./Biginner Python Projects/80.Build a Multi-Task Saver.txt",'r')
k=f.readlines()
for i in k:
    print(i)
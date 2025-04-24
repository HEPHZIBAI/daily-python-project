'''
Project Description
    Create a terminal-based note manager that allows users to add or view notes stored in a text file. 
    Try to use Python 3.10 or newer and use match-case statements.

How the Project Works
    (1) The program starts by prompting the user to choose an option (e.g., 1 for adding a note). 
    (2) The user submits a new note. 
    (3) The program stores the note in a text file in the background and lets the user choose an option again. 
    (4) If the user chooses 2, all the notes should be displayed on the screen.

'''
choice=0

while True:
    print("\nMenu:\n1. add a note\n2. view all notes\n3. exit\n")
    choice=int(input("choose an option (1,2, or 3) : "))
    if choice==1:
        note=input("enter your notes : ")
        with open("./Beginner Python Projects/17.Build a Simple Note Taker.txt",'a') as f:
            f.write(note+"\n")
        print("note added")    
    elif choice==2:
        print("notes list: ")
        with open("./Beginner Python Projects/17.Build a Simple Note Taker.txt",'r') as f:
            for i in f.readlines():
                print("-"+i)
    else:
        break
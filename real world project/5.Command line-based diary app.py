'''
Project Brief
    Your task for this project is to create a command line-based diary program.

Project Instructions
    Write a program that:
    Asks the user to enter the notes of today:
    The user can type in a line, press Enter, type in the next line, press Enter, and so on.
    If the user types in “exit” and presses Enter, the program exits.
    When the program exits, the notes are saved in a text file. The name of the text file should be today’s date (e.g., 2024-03-20.txt).

'''

from datetime import date

name=date.today()
print("enter your notes for today. type 'exit' to save and exit.\n")
f=open(f"./real world project/5.Command line-based diary app/{name}.txt",'a')


while True:
    t=input().strip()
    
    if t=="exit":
        break

    f.write(t)

print(f"your notes have been saved to {name}.txt")
'''
Project Overview 💡
    In this project, you’ll build a simple note-taking application that saves user input into a file named with the current date. 
    This is a great way to practice working with dates, file handling, and user input in Python.

Task:
    Write a Python script that:
    Retrieves today’s date
    Prompts the user to enter notes line by line
    Stops input when the user types "exit"
    Saves the content to a text file named YYYY-MM-DD.txt

Expected Output:
    The program prompts the user in the terminal to enter some notes.
    The user can enter as many notes as they want. Once they type in and submit “exit”, the program prints out a confirmation that the notes were saved in a text file and it also creates a text file where the notes are saved.
'''

from datetime import date

name=date.today()
print("enter your notes for today. type 'exit' to save and exit.\n")
f=open(f"./real world project/313.Save Daily Notes to a Dated File/{name}.txt",'a')


while True:
    t=input().strip()
    
    if t=="exit":
        break

    f.write(t)

print(f"your notes have been saved to {name}.txt")
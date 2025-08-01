'''
Today, you’ll build a program that scans a text file of names and finds every line that starts with a given first name.
It’s a small script, but you’ll learn 
    file handling, 
    string splitting,
    filtering — 
    
Project Description
    Your task today is to build a small, practical Python app that searches through a text file containing a list of names and surnames, and prints out all the full names that have a specific given name (the first word in each line).
    But this time, instead of making your own text file, you’ll use a real dataset provided for you.

It’s a simple .txt file hosted on Google Drive that looks like this:
    Alejandro Morales
    John Smith
    Hiroshi Tanaka
    Ekaterina Ivanova
    Luca Bianchi
    Amara Diallo
    Liam O’Connor
    Sofia Petrova
    Omar Al-Masri
    John Doe
    ...

So if the user types John, it will find and display:
    These are all the names starting with 'John':
    John Smith
    John Doe

This is exactly the kind of lightweight program you might write to:
    Filter a raw text export from a database,
    Quickly look up all records for a given first name,
    Or do informal audits of membership or contact lists.

Expected Output
    If the name isn’t found:

💡 Hint
    Open and read each line of the file,
    Split lines into words to get the first name,
    Compare it to the user’s input in a case-insensitive way,
    And keep track of all matches in a list to print at the end.
    🔍 It also reminds you to .strip() each line to clean up newlines.
'''

name=input("enter the name to look for: ").strip()
a=[]

with open("./Beginner Python Projects/111.Find All Names Starting with John in a Text File.txt",'r') as f:
    b=f.readlines()
    for i in b:
        k=i.strip().split()
        if k[0]==name:
            a.append(i.strip())

if len(a)==0:
    print(f"No names found starting with\n'{name}'.")
else:
    print(f"these are all the names starting with '{name}'")
    for i in a:
        print(i)
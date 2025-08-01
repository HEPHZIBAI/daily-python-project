'''
Your task for today is to build a contact book in Python that stores names, phone numbers, and email addresses in a CSV file. 
This project will teach you how to gather user input, work with CSVs, and display stored data — all useful skills for handling structured information.

📝 Project Task
    The program should:
        Prompt the user to enter a name, phone, and email.
        Save the information to a .csv file (e.g. contacts.csv).
        Add a feature to display all saved contacts (formatted nicely in the terminal).
    This is a great real-world use case of Python’s built-in csv module and a chance to practice building simple utilities that persist data.

📌 Expected Output
    When you run the program, it should:
        Ask the user to input name, phone, and email.
        Save that data to a CSV file.
        Ask if the user wants to view all saved contacts.
        If yes, it should print all contacts from the CSV.

Example interaction in the terminal:
    Enter name: Alice
    Enter phone: 123456789
    Enter email: alice@example.com
    Contact saved.
    View all contacts? yes
    Name: Alice
    Phone: 123456789
    Email: alice@example.com
That will generate a contacts.csv file:
'''

import csv

with open("./new/517b.CSV Contact Book.csv",mode='r+') as f:
        reader=csv.reader(f)
        row_count = sum(1 for row in reader)
        writer=csv.writer(f)
        writer.writerow(["name","phone","email"])

name=input("enter name: ").strip()
phone=int(input("enter phone: "))
email=input("enter email: ").strip()
print("contact saved.")

with open("./new/517b.CSV Contact Book.csv",mode='a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow([name,phone,email])

a=input("view all contacts? ").strip()

if a=="y":
    with open("./new/517b.CSV Contact Book.csv",mode='r') as f:
        reader=csv.reader(f)
        header=next(reader,None)
        
        for i in reader:
            if i:
                print("Name : ",i[0])
                print("Phone: ",i[1])
                print("Email: ",i[2])
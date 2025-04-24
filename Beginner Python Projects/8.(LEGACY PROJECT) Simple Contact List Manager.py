'''
Project Description
    Create a program that lets the user submit names and phone numbers through the console and stores those numbers in a text file.

How the Project Works
    (1) The program prompts the user to enter a name (e.g., John Smith) and then a phone number (e.g., 0011220011). 
    (2) The program keeps asking the user to enter more names and phone numbers until the user enters “done”. 
    (3) If the user enters “done”, the program creates a new “contacts.txt”* file and saves the data there.
    *Here is how the generated text file would look like:

Project Skills Needed
    This project covers the following concepts. Click any link to learn more about them if you're unfamiliar.
    input() function | print() function | strings |lists| dictionaries | if-else conditionals | while-loops
'''
while True:
    name=input("enter contact name (or type 'done' to finish): ").strip()
    if name=='done':
        break
    phone=input(f"enter phone number for {name}: ").strip()
    with open("./Beginner Python Projects/8.(LEGACY PROJECT) Simple Contact List Manager.txt",'a') as f:
        f.write(name+":"+phone)

print("contacts saved.")
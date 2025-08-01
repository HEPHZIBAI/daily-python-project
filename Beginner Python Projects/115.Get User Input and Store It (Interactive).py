'''
Your task for today is to build a simple Python program that repeatedly asks the user for input and stores each response in a text file. 
This exercise will help you get comfortable with working with input/output in Python and handling text files — a fundamental skill in many real-world applications.

📝 Project Task
    The program should:
        Repeatedly prompt the user to type something.
        Save each input to a file (one input per line).
        Stop asking when the user types "exit" (case-insensitive).
    This type of pattern — getting user input and writing it to a file — is useful for things like logs, note-taking apps, or command-line tools.

📌 Expected Output
    When you run the program in the terminal, it should:
        Ask the user to type a message.
        Save each message into a file like notes.txt.
        Stop only when the user types "exit" (or "EXIT", etc.).

Here’s an example of the interaction:
    What do you want to write? Buy milk
    What do you want to write? Call mom
    What do you want to write? Exit
    The notes.txt file should then contain:
        Buy milk
        Call mom
'''
f=open("./Beginner Python Projects/513b.Get User Input and Store It (Interactive).txt",'a')
while True:
    a=input("what do you want to write? ").strip()
    if a!="exit":
        f.write(a+"\n")
    else:
        break
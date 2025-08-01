'''
Your task for today is to write a Python program that saves a quote entered by the user and then reads it back from a file. 
This simple project introduces you to basic file input/output — a key Python skill used in everything from logging to data processing.

📝 Project Task
    The program should:
        Ask the user to input their favorite quote.
        Save the quote to a .txt file (e.g. quote.txt).
        Read the quote back from the file.
        Print the retrieved quote.
    This is a gentle and practical introduction to working with text files in Python — one of the most common tasks in everyday scripting and automation.
    When you run the program, it should:
        Prompt the user for a quote.
        Write the quote to a file.  
        Read the content of that file.
        Display the quote back to the user.

Example:
    What is your favorite quote? Stay hungry, stay foolish.
    Saved and loaded quote: Stay hungry, stay foolish.
'''

quote=input("What is your favorite quote? ").strip()
f=open("./new/516b.Write and Read a Quote.txt",'a')
f.write(quote+"\n")
print("saved and loaded quote: ",quote)
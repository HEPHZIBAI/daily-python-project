'''
Project Description
    Create a Python program to count the occurrences of any given word in the book stored in this text file.

Expected Output
    The user can enter any word (e.g., snow), and the program should find out how many occurrences of that word exist in the book.txt file and print out a message:

Learning Benefits
    File Handling: Learn how to open, read, and close text files.
    String Manipulation: Practice working with strings and string methods like split(), count(), etc.
    Input and Output: Learn to take user input and display output to the console.
'''

word=input("enter the word to count: ").strip()
sum=0
book=""

with open("138.Count Any Word in a Book.txt",'r',encoding='utf-8') as f:
    for i in f.readlines():
        book+=i

print(f"the word \'{word}\' appears {book.count(word)} times in the file")
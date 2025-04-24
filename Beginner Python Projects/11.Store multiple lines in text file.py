'''
Project Description
    Create a program that stores data in a text file.

How the Project Works
    (1) Your program should ask the user to enter three sentences:
    (2) Once the user has submitted the sentences, the program prints out a message saying that the sentences have been saved in a text file.
    (3) The sentences are stored in a text file and there should be dash lines between the sentences. Here is what the text file should look like:

Project Skills Needed
    This project covers the following concepts. Click any link to learn more about them if you're unfamiliar.
    input() function | print() function | strings
'''
sent1=input("enter sentence 1: ")
sent2=input("enter sentence 2: ")
sent3=input("enter sentence 3: ")
print("sentences have been saved")

with open("./Beginner Python Projects/11.Store multiple lines in text file.txt",'a') as f:
        f.write(sent1)
        f.write("\n-----------\n")
        f.write(sent2)
        f.write("\n-----------\n")
        f.write(sent3)
        f.write("\n-----------\n")
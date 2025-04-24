'''
Project Description
    This project involves creating a program that takes a sentence as input and counts the number of words in that sentence. 
    The program will also identify the longest word in the sentence.

Learning Benefits
    This project will help you practice string manipulation and introduce you to list operations in Python. 
    By counting words and finding the longest word, you will enhance your problem-solving skills and gain confidence in handling text data.

How the Program Works
    The program prompts the user to enter a sentence. 
    Then, the program returns a message followed by the number of words in the sentence given by the user. 
    In the last line, the program also displays the word that contains more letters in the given sentence.
'''

sent=input('enter a sentence: ').split()
print("the number of word in the sentence is :",len(sent))

l=""

for i in sent:
    if len(i)>len(l):
        l=i

print("the longest word in the sentence is :",l)
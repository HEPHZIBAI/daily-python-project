'''
Project Description
    Create a program where users can add a word and the translation for that word through a command line interface. The program saves the results in a CSV file. This could be useful for someone who is learning new words in a foreign language and wants to create a vocabulary.

How the Project Works
    (1) The program prompts the user to enter a word. The user enters “desk” and presses Enter. 
    (2) The program prompts the user to enter a translation for that word in a foreign language. 
    (3) The program repeats the process by prompting the user to enter another word. 
    (4) If the user enters “done”, the program closes and adds the data to a CSV file*.
    *Here is how the generated CSV file would look like:

Project Skills Needed
    This project covers the following concepts. Click any link to learn more about them if you're unfamiliar.
        input() function | print() function | strings |lists| dictionaries | if-else conditionals | while-loops

Prerequisites
    Required Libraries: csv (standard library - no need to install)
'''

import pandas as pd

word=""
trans=""
word1=[]
word2=[]

while True:
    word=input("enter a word in language 1 (or type 'done' to finish): ").strip()
    if word=="done":
        break
    trans=input("enter the translation of 'king' in language 2: ").strip()
    
    word1.append(word)
    word2.append(trans)

    print(f"'{word}' (langurage 1) has been added with the translation: '{trans}' (langurage 2)\n")

print("your bilingual vocabulary list:")

df=pd.DataFrame({"language 1":word1,"language 2":word2})
df.to_csv("./Beginner Python Projects/6.(LEGACY PROJECT) Build a Bilingual Vocabulary.csv",index=False)
print("\nYour Bilingual Vocabulary List:")
print(df.to_string(index=False))

print("the vocabulary has been saved to 'bilingual_vocabulary.csv' ")
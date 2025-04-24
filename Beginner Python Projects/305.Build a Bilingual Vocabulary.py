'''
Project Overview 💡
    In this project, you’ll build a bilingual vocabulary tool that allows users to enter word pairs in two languages and save the vocabulary to a CSV file. 
    This is a practical project for learning how to use dictionaries, loops, and CSV file handling in Python.

Task:
    Write a Python script that:
    Continuously prompts the user to enter a word and its translation
    Stores the word pairs in a dictionary
    Saves the dictionary to a CSV file
    Displays the vocabulary list at the end

Expected Output: 
    The user enters a word in English (e.g., “king”) and its translation to another language (e.g., “mbret”). 
    The user can enter as many word pairs as they want.
    The program prints the complete bilingual dictionary to the terminal and saves the files in a CSV file which looks like this:

Comparison
    The original version uses a dictionary and provides user feedback after each entry. It uses the csv module to manually write the vocabulary to a file and loops through the dictionary to display the final vocabulary list.
    The alternative version uses two lists and a pandas DataFrame, offering better integration with data analysis tools and a more concise saving and display process. It simplifies file output with to_csv() and improves readability when showing the final vocabulary list.
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
df.to_csv("./Beginner Python Projects/305.Build a Bilingual Vocabulary.csv",index=False)
print("\nYour Bilingual Vocabulary List:")
print(df.to_string(index=False))

print("the vocabulary has been saved to 'bilingual_vocabulary.csv' ")
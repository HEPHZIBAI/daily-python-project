'''
Project Overview 💡
    In this project, you'll build a simple text analyzer in Python. 
    You'll learn how to process text, count words, sentences, and characters, and identify the most frequent word. 
    This is a great exercise in string manipulation and working with dictionaries.

Task:
    Write a Python script that takes a user-inputted block of text and analyzes it by calculating the number of characters, words, and sentences. 
    Additionally, determine the most frequently used word and calculate the average word and sentence length.

Expected Output:
    The program should output text statistics, including:
    Total Characters
    Total Words
    Total Sentences
    Most Frequent Word
    Average Word Length
    Average Sentence Length

you can use text:
    Trees usually reproduce using seeds. Flowering plants have their seeds inside fruits, while conifers carry their seeds in cones, and tree ferns produce spores instead.
'''

sent=input("enter a block of text for analysis:\n").strip().lower()
s=" "+sent[::]+" "
avg=0
word="   "
punctuation = ".,!?:;'\"()[]{}"
for char in punctuation:
    s = s.replace(char, "")

for i in list(set(s.split())):
    avg+=(len(i)*(s.count(i)))
    i=' '+i+' '

    if s.count(i)>s.count(word):
        word=i



print("text analysis results: ")

print("total characters:",len(sent))
print("total words:",len(sent.split()))
print("total sentence:",sent.count('.')+sent.count('!')+sent.count('?'))
print("most frequent word:\'",word,"\' (used",s.count(word),"times)")
print("average word length:",avg/len(sent.split()),"characters")
print("average sentence length:")
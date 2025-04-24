'''
Project Description
    This program defines a string, counts how many vowels and consonants are present, and displays both counts.

How the Project Works
    Start your script by defining a sentence as a string. 
    Here is an example:
        text = "How many vowels and consonants are in this sentence?"
Here is how the program behaves when run:
'''

text = "How many vowels and consonants are in this sentence?"
v=0
c=0

for i in text.lower():
    if i in "aeiou":
        v+=1
    elif i>='a' and i<='z':
        c+=1

print("the number of vowels in the string is: ",v)
print("the number of consonants in the string is: ",c)
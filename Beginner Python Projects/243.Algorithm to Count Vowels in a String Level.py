'''
Project Description
    This program defines a string and counts how many vowels (a, e, i, o, u) are present in that string. 
    It then displays the count of vowels.

How the Project Works
    Start your script by defining a sentence as a string. 
    Here is an example:
    text = "Hello, how many vowels are in this sentence?"
    Here is how the program behaves when run:
'''

text = "Hello, how many vowels are in this sentence?"
    
v=0

for i in text.lower():
    if i in "aeiou":
        v+=1

print("the number of vowels in the string is: ",v)
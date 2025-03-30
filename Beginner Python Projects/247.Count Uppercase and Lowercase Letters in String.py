'''
Project Description
    This program defines a string, counts how many uppercase and lowercase letters are present, and displays both counts.

How the Project Works
    Start your script by defining a sentence as a string. 
    Here is an example:

    text = "This Sentence Has Mixed CASE Letters!"
    Here is how the program behaves when run:
'''

text = "This Sentence Has Mixed CASE Letters!"
u=0
l=0

for i in text:
    if i>='A' and i<='Z':
        u+=1
    elif i>='a' and i<='z':
        l+=1

print("the number of uppercase letters is: ",u)
print("the number of lowercase letters is: ",l)
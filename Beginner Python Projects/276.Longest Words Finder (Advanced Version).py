'''
Project Description
    In a previous beginner’s project, we built a program that identified the longest word from a given list. 
    Today’s program is an advanced version of the beginner’s version as it gets the list items from the user through user input instead of having the lists hardcoded in the program.
    Specifically, the program:
        Allows the user to input a list of words in the terminal and let them specify the minimum word
    Identifies the longest word(s) in the list, including multiple words with the same maximum length and prints out a message that includes the number of characters of that word:

Learning Benefits
    You will practice handling user input, 
    list manipulation, filtering data, and 
    working with conditional logic to handle multiple longest words.
    You will also be able to expand on this project by adding additional features such as sorting the words alphabetically or 
    counting the occurrences of each word.
'''

listword=input("Enter a list of words separated by spaces: ").split()
l=0
g={}

for i in listword:
    if len(i) not in g:
        g[len(i)]=[]
    g[len(i)].append(i)
    if len(i)>l:
        l=len(i)

print(f"the longest word(s) with {l} characters:")
for i in g[l]:
    print('-',i)
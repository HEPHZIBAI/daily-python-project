'''
Project Description
    Write a program that takes a list of words and finds the longest word in that list. 
    The program should also display the length of that word.
    Start by placing the following list in your script:
    words = ["apple", "banana", "cherry", "blueberry"]
    Below is what your program should output.
    As you can see above, the program has found the longest word and it has printed out a message which also includes the length of the longest word. 
    It is recommended to use an f-string to construct that message.

Learning Benefits
    String Operations: Practice calculating string lengths using len().
    List Iteration: Get hands-on experience iterating over a list with a for loop.
    f-string: Use f-strings to construct a string out of other strings and variables.
'''
words = ["apple", "banana", "cherry", "blueberry"]

l=0
g={}

for i in words:
    if len(i) not in g:
        g[len(i)]=[]
    g[len(i)].append(i)
    if len(i)>l:
        l=len(i)

print(f"\"{g[l][0]}\" is the longest word with {len(g[l][0])} characters")
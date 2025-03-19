'''
Project Description
    Your task for today is simple. 
    You should make a program that takes a list of tree species found in a forest and counts how many times each species appears.

    trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]

Expected Output
    Here is what your program should print out:

Learning Benefits
    List Processing: Work with lists containing real-world data.
    Dictionary Handling: Understand how to store and retrieve counts dynamically.

'''

trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]
g=[]
for i in trees:
    i=i.strip()
    if i not in g:
        print(i,trees.count(i))
        g.append(i)
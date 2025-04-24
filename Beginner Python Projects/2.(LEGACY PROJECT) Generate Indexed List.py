'''
Project Skills Needed
    This project covers the following concepts. 
    Click any link to learn more about them if you're unfamiliar.
    lists | list comprehensions | tuples | input() function | enumerate() function

Project Description
    This project involves creating a program that takes a list of elements, processes it using list comprehension, and returns a new list that pairs each element with its index in the original list.

How the Project Works
    Add this line on top of an empty Python script:
    mylist = ['a', 'b', 'c']
    In the script, iterate over that list using a for-loop or preferably a list comprehension to produce the following list of tuples:
    [('a', 0), ('b', 1), ('c', 2)]
    Each tuple in this new list consists of an element from the original list paired with its corresponding index.
    The output of the program should be the text “Indexed list:” followed by the newly produced list:
'''

mylist = ['a', 'b', 'c']
g=[]

for i in range(len(mylist)):
    g.append((mylist[i],i))

print(g)
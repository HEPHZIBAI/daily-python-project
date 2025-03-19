'''
Project Description
    Write a program that takes a list of words and finds the most frequently occurring one. 
    Start by writing this list in the first line of your program:

    words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]

Expected Output
    Your program should find the most frequent word and print out a message similar 
    to the following where the most frequent word (i.e., “love“) is is mentioned.

Learning Benefits
    List Processing: Work with lists containing text data.
    Using Collections (Optional): Learn how the Counter class simplifies frequency counting.
    Efficient Lookups: Extract the most common element in a single step.

'''

words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]
g={}
l=0
k=""

for i in set(words):
    g[i]=words.count(i)
    if g[i]>l:
        l=g[i]
        k=i

print("the most frequent word is \'",k,"\' appearing",g[k],"times.")
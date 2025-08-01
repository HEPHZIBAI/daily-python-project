'''
Your task for today is to count unique values in a dictionary. 
This exercise will strengthen your skills in working with dictionaries and analyzing their contents.

Project Task
    Your task is to write a Python program that:
        Starts with a predefined dictionary.
        Extracts all the values from that dictionary.
        Counts how many of those values are **unique**.
        Prints the count of unique values.
    This type of task is a common step in data preprocessing, so mastering it now will give you an edge when working with real-world datasets later on.

Expected Output
    When your program runs, it should print how many unique values exist in the dictionary. 
    For example:
        There are 3 unique values in the dictionary.
    If the dictionary is `{'a': 1, 'b': 2, 'c': 1, 'd': 3}`, then the unique values are 1, 2, and 3.
'''

a={'a': 1, 'b': 2, 'c': 1, 'd': 3}
k=list(set(a.values()))
k.sort()
print(k)
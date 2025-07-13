'''
Project Description
    Your task for today is to write a Python program that swaps the keys and values in a dictionary. 
    That means turning something like {'a': 1, 'b': 2} into {1: 'a', 2: 'b'}.
    This exercise is very useful in real-world Python work. 
    For example, you might have a dictionary where usernames are keys and user IDs are values — and you want to reverse it to look up usernames by ID instead.

In this project, you'll be start by storing a sample dictionary in a variable. 
Here is your dictionary:
    original = {'a': 1, 'b': 2, 'c': 3}
Your goal is to loop through it (or use a one-liner) to build a new dictionary where each value becomes a key, and each key becomes the value.

Expected Output
    If the input dictionary is:
        {'a': 1, 'b': 2, 'c': 3}
    Your program should print:
'''

a={'a': 1, 'b': 2, 'c': 3}
b={}
for i in list(a.keys()):
    b[a[i]]=i

print(b)
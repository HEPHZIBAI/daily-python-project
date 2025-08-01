'''
📝 Project Task
    Your task for today is to write a Python program that merges two dictionaries into a new one.

The program should:
    Start with two predefined dictionaries (you can hardcode them).
    Merge them into a new dictionary.
    Print out the result.

This is a great opportunity to practice both the modern unpacking method and the more traditional update method. Try both!

📌 Expected Output
    When run, your program should output the merged dictionary in the terminal. 
    For example:
        {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''

a1={'a': 1, 'b': 2}
a2={'c': 3, 'd': 4}
a3=a1.copy()
a3.update(a2)
print(a3)
'''
Project Description
    Let’s have another project on lists since they are a key data type in Python whenever we need to store multiple items.
    Your task for today is to write a program that merges two lists into one and removes any common items between them.
    Start by pasting these two lists in an empty Python script:

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]

    Then, add some code so your program should:
    Merge these two lists into one single list.
    Remove the common/duplicate items
    Print out the updated list.

Expected Output
    Here is what the program should print out after you run it:

Learning Benefits
    List Merging: Practice combining multiple lists into one.
    List Comprehension: Use list comprehension to filter elements efficiently.
    Removing Duplicates: Understand how to remove elements that appear in both lists while keeping the unique ones.
'''

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(list(set(list1).symmetric_difference(set(list2))))
'''
Project Description
    Lists are one of the most heavily used datatypes in Python. 
    They are designed to store multiple other Python datatypes such as numbers, strings, and any other type. 
    For today’s task, you need to process the following two lists:

    list1 = [5, 3, 8, 6, 3]
    list2 = [7, 2, 5, 9, 8]
    Specifically, your task is to:
    Place the two lists in a .py file.
    Add some code that combines the two lists into one single list.
    Removes any duplicates from the combined list.
    Sort the combined list in ascending order.
    Print out the sorted list.
    Here is what your program should print out:

Learning Benefits
    List Operations: Practice combining and modifying lists.
    Data Structures: Understand how to use set to remove duplicates.
    Sorting: Learn how to sort lists with the sort() method.
'''

list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]
list=list(set(list1+list2))
list.sort()
print(list)
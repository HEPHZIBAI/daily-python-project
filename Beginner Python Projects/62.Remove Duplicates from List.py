'''
Project Description
    Write a program that removes duplicate items from a list while keeping the original order. 
    The program should return a new list with only unique elements. 
    You can place the following list in your script and then add the code that removes duplicates and 
    prints out the new list.

    numbers = [3, 1, 2, 3, 4, 1, 5, 2]

    We provide two different solutions to this problem behind the “Show Code” button and compare the two discussing which is the best code.

Expected Output
    The program should print out the text “List without duplicates:” followed by the cleaned list.

Learning Benefits
    List Manipulation: Practice handling and modifying lists dynamically.
    Membership Checking: Learn how to check if an item is already present in a list using in.
    Data Cleaning: Understand the importance of removing duplicates when processing data.
'''
numbers = [3, 1, 2, 3, 4, 1, 5, 2]
print(list(set(numbers)))
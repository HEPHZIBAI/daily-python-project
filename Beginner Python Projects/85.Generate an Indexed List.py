'''
Project Overview 💡
    In this project, you’ll learn how to work with Python’s built-in sum() function to calculate the sum of a list. 
    This is an essential skill for working with lists, especially when you’re dealing with datasets or performing calculations in data analysis.

Task:
    Write a Python script that creates a list of elements, pairs each element with its index using the enumerate() function, and stores the results in a new list. 
    Finally, print the indexed list.

Expected Output:
    The program should output the text “Indexed list: ” and the indexed list itself:
    
Step-by-Step Guide
    Step 1️⃣: Define the Original List
        Let’s start by creating a list that contains some elements. We will use a simple list of characters.
        Place this code in line 1:
        mylist = ['a', 'b', 'c']
    Step 2️⃣: Create an Empty List for the Indexed Items
        We need a new list to store our indexed tuples.
        Place this code in line 3:  
        indexed_list = []
    Step 3️⃣: Iterate Over the List with enumerate()
        The enumerate() function helps us loop through a list while keeping track of the index. We will store each element as a tuple in indexed_list.
        Place this code in lines 5-6:
        for idx, item in enumerate(mylist):
            indexed_list.append((item, idx))
    Step 4️⃣: Print the Indexed List
        Finally, let’s print the original list alongside our indexed list.
        Place this code in line 8:
        print("Indexed list:", indexed_list)

Complete Code 🧨
    mylist = ['a', 'b', 'c']
    indexed_list = []
    for idx, item in enumerate(mylist):
        indexed_list.append((item, idx))
    print("Indexed list:", indexed_list)

Extra Challenge 🚀
    Modify the script to allow user input instead of using a predefined list. 
    Ask the user to enter a comma-separated list of values, convert the input into a Python list, and generate an indexed list using enumerate(). 
    Finally, print the indexed list.

What’s Next?
    Now that you’ve learned how to generate an indexed list, try applying enumerate() in other contexts! 
    For example, use it to iterate over a list of student names, product names, or file names while keeping track of their positions.
    This technique is especially useful when working with data processing, automation scripts, and machine learning preprocessing.
'''

mylist = ['a', 'b', 'c']
indexed_list = []
for idx, item in enumerate(mylist):
    indexed_list.append((item, idx))
print("Indexed list:", indexed_list)
'''
Project Description
    Imagine you have a list of ages or transaction amounts, but you want to remove all the numbers that are below a certain threshold—like filtering out low amounts from financial transactions. 
    This project is about removing unwanted numbers and cleaning up your data.

How the Program Works
    Start the program by defining this list at the top of the script:

    numbers = [23, 45, 12, 67, 89, 10, 4, 33]
    Then, add some code that prints out the list without the numbers that are less than 20.
    Here is what the output would look like:
    Pro tip: Use a function that gets a list and a threshold number as arguments and returns the filtered list.

How This Project Matters in the Real-World
    In the real world, you might work with lists of data that need to be cleaned before use. 
    For instance, you may want to remove invalid or low-value entries from financial reports, user surveys, or even scientific data. 
    Such data may be stored in text files, CSV files, etc, but you may load the data from such files into a Python list and then continue using the same technique to remove certain values as the technique used in this project. 
    Find out our solution in the Show Code button down below.

'''

numbers = [23, 45, 12, 67, 89, 10, 4, 33]
    
print(numbers)

print([i for i in numbers if i>20])
'''
Why This Project Matters 💡
    In this project, you’ll learn how to work with Python’s built-in sum() function to calculate the sum of a list. 
    This is an essential skill for working with lists, especially when you’re dealing with datasets or performing calculations in data analysis.

Task:
    Create a function that takes a list as an argument, calculates the sum of the list items, and returns the sum. 
    Then, call the function and print the output.

Expected Output:
    Here is the expected output if I called the function using the list [1, 2, 3, 4, 5]:

Step-by-Step Guide
    Step 1️⃣: Define the Function
        We’ll start by defining a function that will take in a list of numbers and return the sum. 
        This will allow us to easily calculate the sum of any list we provide.
        Place this code in lines 1-2:
            def calculate_sum(numbers):
                return sum(numbers)
    Step 2️⃣: Create a List of Numbers
        Next, we need to create a list of numbers that we’ll use for the calculation. 
        You can customize the list to test with different sets of numbers.
        Place this code in line 4:
            numbers_list = [1, 2, 3, 4, 5]

    Step 3️⃣: Call the Function and Print the Result
        Now, call the calculate_sum() function with the list of numbers, and print the result so you can see the total sum.
        Place this code in line 5:
            print(str(calculate_sum(numbers_list)))
Complete Code 🧨
    def calculate_sum(numbers):
        return sum(numbers)

    numbers_list = [1, 2, 3, 4, 5]
    print(str(calculate_sum(numbers_list)))

Extra Challenge 🚀
    Think of ways you can make the program more robust. 
    For example:
        • Add error handling to check if the list contains any non-numeric values, and handle them appropriately.
        • Modify the function to calculate the sum of only positive numbers, ignoring negative ones.
'''
def sum_of_postive(num):
        return sum(i for i in num if i>0 )

def calculate_sum(numbers):
            return sum(numbers)

numbers_list = [1, -2, 3, -4, 5]
print(str(calculate_sum(numbers_list)))
print(str(sum_of_postive(numbers_list)))
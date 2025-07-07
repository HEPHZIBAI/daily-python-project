'''
Project Description
    Your task today is to build a beginner-friendly Python program that finds the largest number in a list — by writing your own logic instead of using Python’s built-in max() function.
    But there’s a twist: instead of using a hardcoded list, your program should ask the user to input a list of numbers separated by commas.
    You’ll then write a function that loops through the list and determines the largest number by comparing each item. 
    Using functions like this is an essential programming skill. 
    It trains you to break down problems and build code that’s reusable and easy to test.

This same logic is used in countless real-world scenarios, like:
    Finding the highest exam score in a class
    Determining the biggest sale in a dataset
    Checking the peak temperature over a week

Expected Output
    Here’s what a sample run might look like:
    Enter numbers separated by commas: 3, 45, 7, 89, 21
    The largest number is: 89
'''

a=list(map(int,input("enter numbers separated by commas: ").split(',')))

l=0

for i in a:
    if i>l:
        l=i

print("the largest number is :",l)
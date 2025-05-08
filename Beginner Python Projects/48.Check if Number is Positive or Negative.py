'''
Project Description
    Create a simple program that checks if a given number is positive, negative, or zero.

Expected Output
    Any time the program is executed, it prints out different messages based on the number sign:

Learning Benefits
    Conditional Statements: Practice using if-elif-else statements to make decisions based on conditions.
    Input and Output: Practice taking user input and displaying output to the console.
    Comparison Operators: Utilize comparison operators like >, <, and == to compare numbers.
'''
number=int(input("Enter a number: "))

if number > 0:   
        print("The number is positive.") 
elif number < 0:   
    print("The number is negative.") 
else:   
    print("The number is zero.")
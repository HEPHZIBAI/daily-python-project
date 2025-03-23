'''
Project Description
    In a previous project, we created a program that checked if a number was positive or negative, or zero:
    number = float(input("Enter a number: "))  
    if number > 0:   
        print("The number is positive.") 
    elif number < 0:   
        print("The number is negative.") 
    else:   
        print("The number is zero.")

    In this project, your task is to improve that project by:
    (1) Doing the checks inside a function definition and then calling that function.
    (2) Including the number in the messages (e.g., “The number -5 is negative”) as shown in the Expected Output section.

Expected Output

Learning Benefits
    Conditional Statements: Practice using if-elif-else statements to make decisions based on conditions.
    Input and Output: Practice taking user input and displaying output to the console.
    Comparison Operators: Utilize comparison operators like >, <, and == to compare numbers.
'''

def find(number):
    if number > 0:   
        print("The number is positive.") 
    elif number < 0:   
        print("The number is negative.") 
    else:   
        print("The number is zero.")

find(int(input("Enter a number: ")))
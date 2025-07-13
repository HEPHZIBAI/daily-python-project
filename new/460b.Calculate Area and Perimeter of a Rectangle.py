'''
Project Overview 💡
    In this project, you'll create a Python program that calculates both the area and the perimeter of a rectangle using separate functions. This is a foundational exercise that helps reinforce the use of functions, arithmetic operations, and code organization.

Task:
    Write a Python program that:
    Defines a function to calculate the area of a rectangle
    Defines another function to calculate the perimeter
    Calls both functions with sample inputs
    Prints the results

Expected Output:
    Below you can see what the program would output if we called it using the following input values:
    area = rectangle_area(10, 3)
    perimeter = rectangle_perimeter(10, 3)
    As you can see, the program prints out 30 for the area and 26 for the perimeter.

Comparison
    The original version is quick and great for testing or learning.
    The alternative version adds interactivity by allowing users to input their own dimensions.
    
'''

def area(l,b):
    return l*b

def perimeter(l,b):
    return 2*(l+b)

print(area(10,20))
print(perimeter(10,20))
'''
Project Description
    Your task for today is to create a Python program that calculates the area of a circle.

How the Project Works
    The program starts by prompting the user to submit the radius of the circle. 
    Once the user submits a number (e.g., 22), the program displays a message that includes the area of the circle.
    Note that the area is shown with two decimal points.

Prerequisites
    Required Libraries: math (optional)
'''
import math

radius=float(input("enter the radius of the circle: "))
print(f"the area of a circle with radius {radius} is {radius*radius*math.pi}")
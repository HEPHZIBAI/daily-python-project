'''
Project Description
    In this project, you'll create a program that converts a list of temperatures in Fahrenheit to Celsius and vice versa.
    Start the program by pasting this list in the first line of your program:

        temperatures_fahrenheit = [32, 50, 77, 100, 212]
    
    The formula to convert fahrenheit to celsius is (fahrenheit - 32) * 5 / 9

Expected Output
    Running the program should output the original list of temperatures in Fahrenheit and the list of temperatures in Celsius:

How This Project Matters in the Real-World
    This example demonstrates a simple concept but is widely applicable in real-world programming. 
    For instance, you might work with weather APIs that return data in one temperature scale, but your users prefer another. 
    You would load the API data in a list, and then do the conversion of every element using a formula and a list comprehension or a for-loop. 
    In real-world programs, similar logic and code can be used for converting between other units, 
    such as kilometers to miles or kilograms to pounds, 
    enabling you to handle localized preferences or integrate with global systems efficiently. 
    By practicing with temperature conversion here, 
    you're laying the groundwork for understanding unit conversions in broader contexts.

'''


temperatures_fahrenheit = [32, 50, 77, 100, 212]

print("temperatures in fahrenheit:",temperatures_fahrenheit)

temp=[]

for fahrenheit in temperatures_fahrenheit:
    temp.append((fahrenheit - 32) * 5 / 9)

print("temperatures in celsius:",temp)
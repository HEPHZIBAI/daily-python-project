'''
Project Description
    Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin using functions.

How the Program Works
    When executed, the program asks the user to enter a value. 
    For example, in the demo below, the user is entering 10:
    Then, the program asks the user to enter what conversion they want to make (e.g., 3 means celsius to Kelvin)
    Depending on the user’s choice, the program calls the function that does the required conversion (i.e., Celsius to Kelvin in our demo example).
    After the user has entered what conversion they want to make, the program calculates the converted temperature by executing the proper function and prints out the results:
    You should have four functions defined in your script:
        celsius_to_fahrenheit
        fahrenheit_to_celsius
        celsius_to_kelvin
        kelvin_to_celsius

How This Project Matters in the Real-World
    This project introduces the concept of modular programming by organizing code into reusable functions. 
    In real-world scenarios, temperature conversions are commonly used in weather applications, scientific calculations, and industrial systems. 
    Such applications rely on functions to make the code scalable and maintainable. 
    For example, in a weather tracking system, a temperature API might return data in Kelvin, and functions would be used to convert it into user-friendly formats like Celsius or Fahrenheit. 
    Understanding how to break down tasks into smaller, reusable functions is essential for working on larger, real-world projects.
'''

def celsius_to_fahrenheit(n):
    print(f"{n}°C={n*(9/5)+32}F")

def fahrenheit_to_celsius(n):
    print(f"{n}°F={n-32*5/9}C")

def celsius_to_kelvin(n):
    print(f"{n}°C={n+273.15}K")

def kelvin_to_celsius(n):
    print(f"{n}°K={n-273.15}C")

print("temperature converter")
temp=float(input("enter the temperature: "))
print("choose the conversion:\n1.celsius to fahrenheit\n2.fahrenheit to celsius\n3.celsius_to_kelvin\n4.kelvin to celsius")
choice=int(input("enter your choice (1-4): "))

if choice==1:
    celsius_to_fahrenheit(temp)
elif choice==2:
    fahrenheit_to_celsius(temp)
elif choice==3:
    celsius_to_kelvin(temp)
elif choice==4:
    kelvin_to_celsius(temp)
else:
    print("invalid input")
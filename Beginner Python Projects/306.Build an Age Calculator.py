'''
Project Overview 💡
    In this project, you'll create a simple Python program that calculates a person's age based on their birth year and the current year. 
    This project is a great exercise for working with user input, integers, and basic arithmetic.

Task:
    Write a Python program that:
    Asks the user to enter their birth year
    Asks for the current year
    Calculates the user's age
    Prints the result

Expected Output: 
    The program prompts the user to enter their year of birth and the current year and then it returns a message with the user's age.

Step-by-Step Guide
    Step 1️⃣: Get the Birth Year
    Prompt the user to input their birth year. Convert the input to an integer.
    birth_year = int(input("Enter your birth year: "))
    Step 2️⃣: Get the Current Year
    Ask the user for the current year and convert it to an integer as well.
    current_year = int(input("Enter the current year: "))
    Step 3️⃣: Calculate the Age
    Subtract the birth year from the current year to get the age.
    age = current_year - birth_year
    Step 4️⃣: Print the Age
    Display the calculated age using an f-string.
    print(f"You are {age} years old.")

Complete Code 🧨
    # Age Calculator
    # Step 1: Ask the user to enter their birth year
    birth_year = int(input("Enter your birth year: "))
    # Step 2: Ask the user to enter the current year
    current_year = int(input("Enter the current year: "))
    # Step 3: Calculate the user's age
    age = current_year - birth_year
    # Step 4: Display the user's age
    print(f"You are {age} years old.")

Alternative Solution
    Here’s a version that uses Python’s built-in datetime module to automatically get the current year:
    from datetime import datetime
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.now().year
    age = current_year - birth_year
    print(f"You are {age} years old.")

Comparison
    The original version asks the user for both birth year and current year.
    The alternative version automatically detects the current year, making it more user-friendly and less error-prone.
'''

birth=int(input("enter your birth year: "))
current=int(input("enter the current year: "))

print(f"you are {current-birth} years old.")
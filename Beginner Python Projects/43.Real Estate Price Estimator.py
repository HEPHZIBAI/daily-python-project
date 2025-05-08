'''
Project Description
    This is a simple beginner project where the program estimates the price of a property based on the size of the house (in square feet) and its location (city or suburb). 
    The program will help practice basic Python concepts such as user input, conditional statements, and basic calculations.

Expected Output
    The program starts by prompting the user to enter the square feet of the property:
    Next, the program asks to enter “city” or “suburb”. 
    If the user submits “city”, the program should use a price of 250 dollars per square foot. 
    If they submit “suburb”, the program should use a price of 150 dollars per square foot.
    After the user has submitted “city” or “suburb”, the program displays a message where it includes the estimated price for the given property.

Learning Benefits
    User Input: 
        You will practice collecting data from the user using input() and converting it to appropriate types (like float for the property size).
    Conditionals: 
        You will use if, elif, and else statements to make decisions based on user input. For example, choosing the price per square foot based on location.
    Arithmetic Operations: 
        You will perform basic arithmetic (multiplying size by price per square foot) to calculate the estimated price of the property.
    String Handling: 
        You will practice working with strings (e.g., location input) and using the .lower() method to handle case sensitivity.
'''

print("welcome to the real estate price estimator!")
feet=int(input("enter the size of the property in square feet: "))
location=input("enter the location (city or suburb): ").strip()
price=float(0)

if location=="city":
    price=250
elif location=="suburb":
    price=150

print(f"the estimated price for a {feet} sq ft property in the {location} is: ${price*feet}")
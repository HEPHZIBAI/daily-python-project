'''
Project Description
    This project simulates a dice roll by generating a random number between 1 and 6. 
    Each time the program runs, it "rolls the dice" and displays the result. 
    This project introduces students to working with random numbers and basic output formatting.

How the Project Works
    The program will use Python’s random module to simulate rolling a six-sided die. 
    Any time the program runs, it displays am message containing the random number:

Prerequisites
    Required Libraries: random
'''
import random

print(f"you rolled a {random.choice([1,2,3,4,5,6])} !")
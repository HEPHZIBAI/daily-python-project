'''
Project Overview 💡
    In this project, you'll build a countdown timer using Python's time module. 
    The user enters a number of seconds, and the program counts down to zero, updating every second in the terminal. 
    This is a great example of loops, formatting output, and working with time-based functions.

Task:
    Write a Python program that:
    Asks the user to input a duration in seconds
    Displays a countdown timer in mm:ss format
    Prints a message when the timer is done

Expected Output: 
    The program will ask the user to enter a value for seconds (e.g., 10):
    After the user enters the seconds, the program will print out the time every second and then print out “Time’s up!” at the end.

Comparison
    The original version uses end="\r" to overwrite the same line in the terminal.
    The alternative version clears the screen every second, which may be more visually pleasing in some terminals. 
'''
import time

second=int(input("enter the time in secondes: "))

while second>0:
    print(f"00:{second:02d}")
    second-=1
    time.sleep(1)

print("time's up!")
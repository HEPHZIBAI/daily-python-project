'''
    Your task for today is to build a countdown timer in Python that starts from a number entered by the user and counts down to 1 with a 1-second delay between each number. 
    When the countdown finishes, the program displays a final message chosen by the user. 
    This project is a great way to practice loops, time delays, user input, and input validation.

📝 Project Task
    Ask the user to enter a starting number (e.g., 10).
    Count down to 1 using a for or while loop, printing each number with a 1-second delay between prints.
    After the countdown, display a final message like "Time’s up!" or "Go!".

💡 Bonus:
    Add a check to ensure the user enters a positive integer.
    Let the user choose the final message before the countdown begins.
This is a fun utility app that builds up your confidence with loops, timing, and working with user inputs in the terminal.

📌 Expected Output
    When the program runs, it might look like this:
        Enter a starting number: 5
        Enter your final message: Go!
        5
        4
        3
        2
        1
        Go!
    If the user types a non-positive number, it should show a message like:
        Please enter a positive integer.
'''
import time

num=int(input("enter a starting number: "))
message=input("enter your final message: ").strip()

if num<=0:
    print("Please enter a positive integer")
else:
    for i in range(num):
        time.sleep(1)
        print(i+1)
    
    print(message)
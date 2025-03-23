'''
Project Description
    This program helps you keep track of deadlines by allowing you to input a specific date and time. 
    It calculates whether the deadline has already passed, is happening today, or how many days remain until the deadline.

Expected Output
    A) Scenario 1: Deadline not passed
        The program starts by prompting the user to enter a deadline in the YYYY-MM-DD HH:MM format.
        If the submitted deadline is later than the current time and date, the program displays the message “The deadline is in x day(s). Keep working 🚀”
    B) Scenario 2: Deadline passed
        If the submitted date is earlier than today’s date, that means the deadline has passed, and the message “The deadline has passed 😢” is printed out.

Learning Benefits
    Date and Time Handling: 
        You will practice using the datetime module to parse, manipulate, and compare dates and times, a crucial skill for scheduling and time-sensitive applications.
    Input Parsing: 
        You will practice accepting user input and converting it into a usable format using strptime().
    Conditional Logic: 
        You will practice implementing multiple conditional statements to handle various scenarios, such as past, present, and future deadlines.
    String Formatting: 
        You will practice formatting messages dynamically to provide meaningful feedback based on the calculated deadline status.

Prerequisites
    Required Libraries: datetime
'''

import datetime as dt

date=input("enter the deadline (e.g., 2024-11-15 17:00): ")
deadline = dt.datetime.strptime(date, "%Y-%m-%d %H:%M")
current=dt.datetime.now()

if deadline > current:
    days_remaining = (deadline - current).days
    print(f"The deadline is in {days_remaining} day(s). Keep working 🚀")
elif deadline < current:
    print("The deadline has passed 😢")
else:
    print("The deadline is today! Stay focused! 🎯")
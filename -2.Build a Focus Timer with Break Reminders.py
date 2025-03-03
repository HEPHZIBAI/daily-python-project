'''
Project Description
    Create a simple program that helps users maintain focus during work or study sessions using timed intervals, also known as the Pomodoro Technique.

How the Program Works
    The program starts by prompting the user to enter the duration of the session. For example, the user enters 25 (minutes):
    The program asks the user to enter the break duration (e.g., 5 min) and how many sessions the user wants to do (e.g., 2 sessions).
    After this, the program freezes execution by using the sleep() method from the time module until 25 are over.

How This Project Matters in the Real-World
    This program demonstrates the importance of using functions and loops to automate repetitive tasks, a fundamental skill in programming. In real life, tools like this are used by productivity enthusiasts and professionals to structure their work hours, improve concentration, and avoid burnout. While this is a simple implementation, similar concepts are used in advanced task management tools like Focusmate, Trello, or even mobile productivity apps. This project introduces a practical application of time-based automation, which can be scaled to include features like notifications, custom sound alerts, or integration with a to-do list.

Prerequisites
    Required Libraries: time
'''
import time

print("welcome to the focus timer!")
duration = int(input("enter focus session duration (in minutes) : "))
breaktime = int(input("enter break duration (in minutes): "))
session = int(input("how many focus sessions would you like to complete ? "))

for i in range(1,session+1):
    print(f"session {i} of {session}")
    print(f"focus for {duration} minute(s).stay on task!")
    time.sleep(duration*60)
    print(f"congratulations you have completed your {i} session")
    if i<session:
        print("take your break time {breaktime} minutes")
        time.sleep(breaktime*60)
        print("break completed")

print("Great job! You have completed all your sessions. Stay productive!")
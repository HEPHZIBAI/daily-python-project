'''
Python code dictation, simple alarm clock. First line of the script, import the time module. Next line, start defining a function named set underscore alarm, which gets two arguments, hours and minutes. In the first line of the function definition, use the print function to print out the string alarm set for and the hours argument and the minutes argument.
next line of the function definition create a variable named current underscore time which is equal to the method call local time of the time module in the next line of the function definition start defining a while loop the while loop checks if current underscore time dot tm underscore hour is different from argument hours or
current underscore time dot tm underscore min is different from minutes this was the first line of the while loop in the next line reassign the variable current underscore time you should reassign it time dot local time the local time method call with parenthesis next line of the while loop pause the
script for 30 seconds using the sleep method of the time module exit the while loop this is the last line of the function definition in this line print out the string time is up wake up exit the function definition and call the set underscore alarm function by giving two argument values 6 and 30. End of the script.
'''

import time

def set_alarm(hours, minutes):
    print("Alarm set for", hours, minutes)
    current_time = time.localtime()
    while current_time.tm_hour != hours or current_time.tm_min != minutes:
        current_time = time.localtime()
        time.sleep(30)
    print("Time's up! Wake up!")

set_alarm(6, 30)
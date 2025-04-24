'''
Project Description
    Build a countdown timer with Python.

How the Project Works
    (1) The program starts by prompting the user to enter the time in seconds (e.g., 10 seconds). 
    (2) Then, the program starts printing out the seconds (e.g., 00:10, 00:09, etc.) one line every one second. 
    (3) At the end, the program prints out “Time is up!”

Prerequisites
    Required Libraries: time
'''

import time

second=int(input("enter the time in secondes: "))

while second>0:
    print(f"00:{second:02d}")
    second-=1
    time.sleep(1)
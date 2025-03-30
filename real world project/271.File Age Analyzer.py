'''
Project Description
    Today you will build a program that analyzes all the files in a given parent directory and its subdirectories, categorizing the files based on their age 
    (e.g., created less than a week ago, between a week and a month old, or older than a month). 
    It provides a summary report with counts for each category and highlights the oldest and newest files.

Expected Output
    Here is what the program generates when I enter my Downloads folder path (e.g., “Users/your_username/Downloads“ on Mac/Linux or “C:\Users\your_username\Downloads” on Windows) as input:
    As you can see, the program lists the number of files created less than a week ago (17 files), between a week and a month ago (74 files) and more than a month ago (22 files).
    It also prints out the path to the oldest and the newest file.

Prerequisites
    Required Libraries: os datetime
'''

print("welcome to file age analyzer!")
path=input("enter the path of the folder to analyzer:")
print("analyzing file ages.please wait...")
print("--file age analysis report---")
print("analysis complete!")
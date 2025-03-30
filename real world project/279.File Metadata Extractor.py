'''
Project Description
    his Python command-line tool extracts metadata from files in a specified directory and displays it. 
    Metadata includes the file size, creation date, modification date, and file type. 
    Users can see a list of all files in a directory, including files in subdirectories, along with their metadata. 
    The results can also be saved into a CSV file for later use or analysis.

How the program works
    The program lets the user enter a directory path in the terminal where some files are located 
    (e.g., /Users/as/Downloads/myfolder for Mac/Linux or C:\Users\as\Downloads\myfolder for Windows):
    The program displays the list of the filepaths contained in the given directory and their metadata 
    (size, creation date, and type):
    The program also lets the user choose whether to save the metadata results in a CSV file or not:
    Here is how the metadata look in the CSV file:
    Tip: You can extract the file creation time and size using the os library:

    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)

Learning Benefits
    Learn how to work with file metadata using Python's os and datetime modules.
    Understand how to display and organize file information in a structured format.
    Practice saving information into CSV files using Python’s csv module.

Prerequisites
    Required Libraries: os, csv, datetime
'''

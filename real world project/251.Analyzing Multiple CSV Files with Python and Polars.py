'''
Project Description
    Polars is an emerging Python library for data analysis and visualization that is growing and improving fast. 
    Just two days ago, the Polars team together with NVIDIA RAPIDS released GPU acceleration. 
    With GPU-accelerated Polars, programmers can now expect a performance boost of up to 13x compared to Polars on CPU on intensive queries.
    For today’s app, we will practice Polars by processing multiple CSV files.

Before Coding
    Download the CSV files in this link and place them in a folder named “invoices”. 
    Place the “invoices” folder in the same directory with your Python script.

How the Project Works
    (1) The program makes a list of all the CSV files located in the “invoices” directory. 
    (2) Then, the program iterates over the files and loads each file as a Polars dataframe. 
    (3) The program calculates the total of the “Price” column of each file. 
    (4) It also counts the total number of invoices for each file.
    Here is what the program should print out in the command line:

Prerequisites
    Required Libraries: glob, polars
    Installation: pip install polars
    Required Files: Download the required files in the “Before Coding” section.
    IDE: You can use any IDE on your computer to code the project.
'''


'''
Project Description
    In yesterday's project, we used Polars to process some invoice data. 
    Today, we will use the same data, but perform more complex operations. 
    We will calculate the total amount spent by each customer, their total number of purchases, and rank the customers by expenditure.

How the Project Works
    (1) The program makes a list of all the CSV files located in the “invoices” directory and iterates over the files and loads each file as a Polars dataframe. (2) Then, the program calculates and prints out the total number of invoices (i.e., 24) and the total of the Price columns of all files (i.e., $5070.50). (3) Then, the program calculates the total sum spent by each customer in all files and ranks the customers by the amount they have spent. (4) The dataframe created in step 3 is exported to a CSV file and a message is printed out in the command line that the report was saved successfully.
        Here is what the program should print out in the command line:

Prerequisites
    Required Libraries: glob, polars
                        Installation: pip install polars
    Required Files: Download the required files in the “Before Coding” section.
'''
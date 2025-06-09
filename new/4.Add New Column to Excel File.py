'''
Project Brief
    Your task for this project is to create a Python program that alters an Excel file by adding a new column to it.

Project Instructions
    Download the Excel file below.
    The Excel file looks like below:
    Write a Python program that:
        Loads the Excel file as a Pandas dataframe or similar.
        Adds a new column named Total to the data.
        The data of the Total column should be a product of the Price column and the Quantity column (i.e., Price x Quantity).

Generates an output.xlsx file that contains the original data and the new Total column.

Project Expected Output
    The expected output is a newly generated Excel file that contains the new Total column as shown below:


Environment Setup Instructions (in your local IDE)
    👉 Skip to step 5 if you prefer to code this project in an online browser-based IDE or from your mobile phone.
    Download the input.xlsx file provided above.
    Install the required libraries:
    pip install pandas openpyxl
    Execute the main.py file once you have finished coding.

Resources
    You can learn about adding new columns to Excel files in the following short tutorial:
    https://pythonhow.com/how/add-a-new-column-to-an-excel-file/

'''

import pandas as pd
df = pd.read_excel('./real world project/1.Add New Column to Excel File.xlsx')
df['Total']=df["Price"]*df["Quantity"]
df.to_excel('./real world project/1.Add New Column to Excel File added.xlsx', index=False)
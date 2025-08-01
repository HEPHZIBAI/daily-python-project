'''
Project Overview 💡
    In this project, you’ll learn how to use Python’s pandas library to read an Excel file, modify its contents, and save the updated data. 
    This is a crucial skill when working with structured data, such as sales reports or inventory records.

Task:
    Write a Python script that reads an Excel file containing sales data, adds a new column named “Total” that calculates Price × Quantity, and saves the updated data to a new Excel file.
    Please use the Excel file below:
   
Expected Output:
    The program should generate a new file named “output.xlsx” with the additional Total column.
    Here is how the generated Excel document should look like:
'''

import pandas as pd

data=pd.read_excel('301.Add a New Column to an Excel File.xlsx',engine='openpyxl')

data['Total']=data['Price']*data['Quantity']

data.to_excel("301.Add a New Column to an Excel File.xlsx",index=False, engine='openpyxl')

print("File 301.Add a New Column to an Excel File.xlsx updated successfully with the 'Total' column.")
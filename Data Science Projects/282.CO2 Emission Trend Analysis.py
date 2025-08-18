'''
Project Description
    This Python program will analyze a dataset containing CO2 emission levels over the years. 
    The program will allow users to visualize the trends of CO2 emissions, 
    identify any seasonal patterns, and calculate basic statistics (like average levels, max, and min). 
    It will help users understand the impact of human activity on the environment by visualizing the changes in CO2 concentration over time.
    We will use pandas for data manipulation, matplotlib for plotting the data, and seaborn for additional data visualization features.

How the program works
    For this we can use publicly available data like CO2 levels from the Mauna Loa Observatory. 
    Here’s a sample CSV dataset to download.

Expected Output
    The program should generate the following graph from the CSV file linked above. 
    It shows the amount of CO2 in ppm over the last four years.

Learning Benefits
    Learn how to work with real-world scientific data in CSV format.
    Understand how to use pandas for cleaning and analyzing data.
    Visualize trends and patterns in the data using matplotlib and seaborn.
    Calculate and interpret statistical values like average, maximum, and minimum.

Prerequisites
    Required Libraries: pandas, matplotlib, seaborn, pyparsing
                        pip install pandas pyparsing matplotlib seaborn
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv("282.CO2 Emission Trend Analysis.csv")

x=df["Year"]
y=df["CO2_Level"]

print(x,y)

sb.lineplot(x=x,y=y)
plt.title("CO2 Levels Over Time (Mauna Loa)")
plt.xlabel("Year")
plt.ylabel("CO2 Concentration(ppm)")
plt.show()
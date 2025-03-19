'''
Project Description
    In this project, your task is to analyze data from IMDb about movies, their genres, release years, ratings, and more. 
    Download the movies.csv file. Here are the first few rows of that file:

Expected Output
    The goal is to visualize the movie ratings from the data given in the CSV file provided in the link above. 
    Specifically, your program should generate a distribution of movie ratings as below:
    The graph shows the frequency of each rating. 
    For example, the ratings 8.5 and 8.6 are the most frequent ones happening in the CSV file.
    We recommend to use pandas, matplotlib, and seaborn to come up with the above graph.

Learning Benefits
    Learn how to load, analyze, and manipulate movie data using Pandas.
    Understand how to visualize trends over time using line charts.
    Gain skills in data exploration, sorting, and filtering.

Prerequisites
    Required Libraries: pandas, matplotlib, seaborn
                        pip install pandas matplotlib seaborn
    Required Files: Download the movies.csv file.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("167.Movie IMDb Data Analyzer.csv")
ratings=df['Rating']

sns.histplot(ratings)

plt.title("distribution of movie ratings")
plt.xlabel("rating")
plt.ylabel("frequency")
plt.show()
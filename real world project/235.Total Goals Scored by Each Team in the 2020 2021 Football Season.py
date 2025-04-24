'''

Project Brief
Several continental football/soccer championships are taking place at the moment such as the Euro 2024 and 2024 Copa América, so let’s have a project on that sport.

Your task for today is to use Python to plot these UK Premier League football CSV data. See here for a description of the column names of the CSV file to help you easily understand the data.

Specifically, your task is to plot the total goals scored by each team. You can use any plotting library, but the solution provided below uses Matplotlib and Seaborn.

Expected Output
Here is the approximate output you should generate:
'''



'''

Description of football data column names
HomeTeam:

Description: The name of the team that played at home.

Data Type: String

AwayTeam:

Description: The name of the team that played away.

Data Type: String

FTHG (Full Time Home Goals):

Description: The number of goals scored by the home team at the end of the match.

Data Type: Integer

FTAG (Full Time Away Goals):

Description: The number of goals scored by the away team at the end of the match.

Data Type: Integer

TotalHomeGoals:

Description: The total number of goals scored by the home team across all matches in the dataset.

Data Type: Integer

Note: This column is created during the data analysis step by aggregating FTHG values for each home team.

TotalAwayGoals:

Description: The total number of goals scored by the away team across all matches in the dataset.

Data Type: Integer

Note: This column is created during the data analysis step by aggregating FTAG values for each away team.

TotalGoals:

Description: The total number of goals scored by each team (both home and away) across all matches in the dataset.

Data Type: Integer

Note: This column is created by summing TotalHomeGoals and TotalAwayGoals for each team.

'''
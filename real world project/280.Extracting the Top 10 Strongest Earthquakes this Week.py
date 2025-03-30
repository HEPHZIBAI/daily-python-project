'''
Project Description
    This project fetches real-time earthquake data from the USGS (United States Geological Survey) API and 
    displays the 10 strongest earthquakes from the past week. 
    It provides useful insights into the most powerful earthquakes worldwide.

How the program works
    The program makes an API request to the United States Geological Survey API at the following endpoint:
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson
    That link returns global earthquakes during the current week.
    Then, the program displays the 10 strongest earthquakes of the week showing information such as the location and 
    the link of the earthquake for more information about that particular earthquake.

Learning Benefits
    Understand how to retrieve real-time data from an API.
    Learn how to process and sort data using Pandas.
    Gain insights into global earthquake activity.

Prerequisites
    Required Libraries: pandas, requests
                        pip install pandas requests
'''

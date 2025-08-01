'''
Project Description
    In the previous project we extracted the top 10 strongest earthquakes around the globe during the current week. 
    Today we will expand this project further by displaying the global earthquakes on a map with Python.

How the program works
    1.Similar to the previous project, the program makes an API request to the United States Geological Survey API at the following endpoint to get all the earthquakes that occured during the current week:
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson
    
    2.The program plots the earthquake locations on an interactive world map using Folium.

Learning Benefits
    Learn how to visualize geospatial data using Folium.
    Understand how to fetch and process API data for visualization.
    Gain experience with interactive map generation.

Prerequisites
    Required Libraries: pandas, requests, folium
    Required Files: No files are required.
'''
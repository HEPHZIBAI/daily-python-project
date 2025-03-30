'''
Project Description
    For this project, we will build a web app using the Python FastHTML web framework.
    We will build a one-page website. 
    On the website, we will display some Python code (as shown above) with its syntax highlighted accordingly and a button for visitors to copy the code.
    This app can serve to share code with other people. 
    Here is what the output looks like.

    Folium Code Snippet
        Feel free to use the following code as you wish:

            import folium
            import pandas as pd
            # Load the CSV file containing country names and coordinates

            def load_data():
                return pd.read_csv("europe.csv")
            
            data= load_data()
            # Create a Folium map centered around Europe
            m = folium.Map(location= [data ["Latitude"].mean(), data ["Longitude"].mean()], zoom
            # Add country names as labels to the map

            for row in data.iterrows():
                folium.Marker(
                    location=[row["Latitude"], row["Longitude"]],
                    popup=row["Country"],
                    tooltip row["Country"],
                    ).add_to(m)
            m.save("map.html")

Learning Benefits
        This project leverages the Python FastHTML web framework, a powerful tool for building fast, efficient, and scalable web applications with minimal setup. 
        FastHTML is specifically designed for developers who want to create modern web apps using Python only, eliminating the need for additional languages or complex configurations. It combines ease of use with the performance necessary for handling larger projects, making it ideal for both beginners and experienced developers looking to enhance their skills in web development.

Expected Output
    Prerequisites
        Required Libraries: fasthtml
                            pip install python-fasthtml

'''
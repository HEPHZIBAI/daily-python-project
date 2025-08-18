'''
Project Brief
    For this project, we will build a RESTful API using FastAPI that simulates a simple weather forecast service. 
    This API will allow users to request a weather forecast for a specified city over a 3-day period. 
    Additionally, users can retrieve the weather forecast for a specific day within this period. 
    The purpose of this project is to introduce you to API development using FastAPI, which is a modern, fast (high-performance) web framework for building APIs with Python 3.6 and above.

Expected Output
    1. The user can query 3-day forecast data for different cities:
        For example, visiting http://127.0.0.1:8000/forecast/London will return 3-day forecasts as shown below:
    2. The user can also query a certain day in the next 3 days. 
        For example, querying day 2 by visiting http://127.0.0.1:8000/forecast/London/2 would return the following data:
    
    Note that to keep it simple, we are generating fake data. 
    Here is a structure of the code to get you started:

    from fastapi import FastAPI
    from random import randint, choice

    app = FastAPI()

    # Sample weather conditions for simulation
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]

    @app.get("/forecast/{city_name}")
    async def get_weather_forecast(city_name: str):
    """Get a 3-day weather forecast for a specific city."""
        ...

        return {"city": city_name, "forecasts": forecast_data}

    @app.get("/forecast/{city_name}/{day}")
    async def get_specific_day_forecast(city_name: str, day: int):
        """Get the forecast for a specific day in the 3-day range."""
        ...

        return {"city": city_name, "forecast": forecast}

Prerequisites
    Required Libraries: fastapi, unicorn
                        pip install fastapi uvicorn
    Required Files: No files are required for this project.
    Running the API: To run the API, you need to execute:
        uvicorn weather_api:app --reload
    where weather_api is the name of your Python script and app is the name of the variable associated to the FastAPI() instance.
'''


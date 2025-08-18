'''
Project Description
    Today we will build the following weather dashboard web app:
    Users can search for a city in the text box and the current weather information for that city will be displayed below the button:
    You can use the Open Weather API to get current weather data. You need to sign up for a free account and get an API key. Then, build a Flask web app that makes API requests to the http://api.openweathermap.org/data/2.5/weather endpoint and display the received JSON data to the webpage.
    To help you solve this project, here is is the script of a previous similar project where we built a command line app to get the current weather of any city using the Open Weather API:

    import requests
    # Replace with your OpenWeatherMap API key
    API_KEY = "141710af2113bab9f55ef73e1bcd33d5"

    def get_temperature(city):
        """Fetches the current temperature for a given city.

        Args:
            city: The name of the city to get weather data for.

        Returns:
    A string containing the current temperature in Celsius or None if an error occurs.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        return f"Current temperature in {city}: {temp:.1f}°C"
    else:
        print(f"Error: {response.status_code}")
        return None


    if __name__ == "__main__":
        city = input("Enter City: ")

        temperature = get_temperature(city)
        if temperature:
            print(temperature)
        else:
            print("Failed to retrieve temperature.") 
    However, today’s project is more advanced since it involces a web app interface.

Learning Benefits
    Learn how to interact with a public API.
    Work with JSON data and extract relevant information.
    Display dynamic data on a web page using Flask.
    Understand how to handle API keys and environment variables for security.
    Improve your ability to build interactive web applications with external data.

Prerequisites
    Required Libraries: requests, flask
                        pip install flask requests
'''

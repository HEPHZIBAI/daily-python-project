'''
Project Description
    In yesterday’s project we build a command line interface (CLI) AI based on the Google Gemini models:
    
    import google.generativeai as genai
    # Replace 'YOUR_API_KEY' with your actual Gemini API key
    genai.configure(api_key='YOUR API KEY')
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    print("Gemini is ready! Type 'exit' to quit.")

    while True:
        user_input = input("Me: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = model.generate_content(user_input)
        print("Gemini:", response.text)
    
    Today, we will build a web app version where users can interact with the AI from using a user-friendly interface directly from their browser.

Here is how the app will look like:
    We will use the Python Flask framework to build this web app. 
    The solution provided in the “Show Code” button down below provides the Python code and also the HTML and Javascript code needed to implement the frontend. 
    It also includes the complete steps to get the app up and running.

Prerequisites
    Required Libraries: google-generativeai, flask
                        pip install google-generativeai flask

'''
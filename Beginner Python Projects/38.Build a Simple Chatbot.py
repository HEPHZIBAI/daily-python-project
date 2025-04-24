'''
Project Objective
    Create a basic chatbot that can respond to a limited set of questions or keywords. 
    This chatbot will analyze user input and give predefined responses based on keywords it detects.

Learning Benefits
    In this project, you will enhance your understanding of control flow and data structures by creating a chatbot that uses dictionaries for keyword-response mapping. 
    This will also give you hands-on experience with user input handling and string manipulation.

How the Program Works
    The program starts by greeting the user, and letting them know they can type “bye” to exit the program.
    The user can ask simple questions such as “what’s the time” or “what is Python” and the chatbot responds. 
    The answers are fetched from a Python dictionary inside the script:
    # Define some responses for keywords 
    responses = {"hello": "Hello! How can I help you today?",
                "hi": "Hi there! What’s on your mind?",     
                "weather": "I'm not sure about the weather, but it’s always a good day to code!",     
                "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",     
                "day": f"Today is {datetime.datetime.now().strftime('%A')}.",     
                "python": "Python is a versatile programming language, great for web development, data science, and more.",     
                "bye": "Bye! Have a great day!", }
You can start with the above dictionary and implement the rest of the program.

Prerequisites
Required Libraries: datetime
'''
import datetime

responses = {"hello": "Hello! How can I help you today?",
                "hi": "Hi there! What’s on your mind?",     
                "weather": "I'm not sure about the weather, but it’s always a good day to code!",     
                "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",     
                "day": f"Today is {datetime.datetime.now().strftime('%A')}.",     
                "python": "Python is a versatile programming language, great for web development, data science, and more.",     
                "bye": "Bye! Have a great day!", }

read=""
print("chatbot: hello! i'm here to chat. type 'bye' to exit")

while read!="bye":
    read=input("you : ").strip().lower()

    if "hello" in read:
        print("chatbot: ",responses["hello"])
    elif "hi" in read:
        print("chatbot: ",responses['hi'])
    elif "weather" in read:
        print("chatbot: ",responses['weather'])
    elif "time" in read:
        print("chatbot: ",responses['time'])
    elif "day" in read:
        print("chatbot: ",responses['day'])
    elif "python" in read:
        print("chatbot: ",responses['python'])
    elif "bye" in read:
        print("chatbot: ",responses['bye'])
    else:
        with open("119.Build a Simple Chatbot.txt",'a') as f:
            f.write(read+'\n')
        print("chatbot: this is not avalible now we have noted and give u best response")
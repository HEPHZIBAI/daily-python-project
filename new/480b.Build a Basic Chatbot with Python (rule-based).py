'''
Project Description
    Your task for today is to build a basic chatbot in Python — one that replies to user input based on a set of predefined rules.
    This chatbot will be rule-based, meaning it doesn't use AI or machine learning, but simply looks at what the user types and responds accordingly. 
    While this may sound simple, it's exactly how many early bots worked — and it's a great way to understand how natural language processing starts.
    Your chatbot should run in a loop and continue interacting with the user until the user types "bye". 
    For example, if the user says "hello", the bot can respond with "Hello there!", and for "how are you", it might say "I'm just code, but thanks for asking!". 
    If the user types something it doesn't recognize, the bot can reply with a default response like "Sorry, I don't understand that."
    This kind of chatbot can be extended later into more advanced bots, but it's also useful on its own for:
        Creating command-line helpers
        Adding interactivity to games or apps
        Practicing basic logic and string handling in Python
        Building a conversational UI for very specific tasks (like customer service FAQs)

Expected Output
    Here’s what a short conversation with your chatbot might look like:
'''

print("Hi! I'm ChatBot. Type 'bye' to exit.")
dict={"hello":"Hello there!", 
      "how are you":"I'm just code, but thanks for asking!",
      "d":"Sorry, I don't understand that.",
      "bye":"Goodbye!"}

while(True):
    you=input("You : ").strip().lower()
    if you not in dict:
        you='d'
    print("ChatBot:",dict[you])
    if you=='bye':
        break
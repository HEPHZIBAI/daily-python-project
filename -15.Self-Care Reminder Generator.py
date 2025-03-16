'''
Project Description
    Write a program that gently suggests self-care activities for the day. 
    The program randomly selects an activity from a predefined list of calming, relaxing actions to promote mental well-being.

    self_care_activities = [
        "Take a short walk in nature. 🌿",
        "Drink a big glass of water. 💧",
        "Do some deep breathing for 5 minutes. 🧘‍♂️",
        "Listen to your favorite music. 🎵",
        "Write down three things you're grateful for. ✨",
        "Read a chapter from a book you love. 📚",
        "Stretch your body gently. 🤸‍♀️",
        "Spend a few minutes with a pet or a loved one. 🐾",
        "Watch the sunset or sunrise. 🌅"
    ]

How the Program Works
    Anytime you run the program, it generates a self-care suggestion you can do at some point in your day. 
    For example:
    If you run it again, it will randomly select another self-care activity from a list of pre-defined activities.
    And here is another run:

    To help you get started, you can use the following list of activities:

Learning Benefits
    Random Module: Practice using random.choice() to select an item from a list.
    Lists: Gain experience creating and working with lists of strings.
    Positive Messaging: Create a feel-good program that’s beginner-friendly and impactful.

Prerequisites
    Required Libraries: random library 
'''

self_care_activities = [
    "Take a short walk in nature. 🌿",
    "Drink a big glass of water. 💧",
    "Do some deep breathing for 5 minutes. 🧘‍♂️",
    "Listen to your favorite music. 🎵",
    "Write down three things you're grateful for. ✨",
    "Read a chapter from a book you love. 📚",
    "Stretch your body gently. 🤸‍♀️",
    "Spend a few minutes with a pet or a loved one. 🐾",
    "Watch the sunset or sunrise. 🌅"
]

import random

print("Hello! Here's your self-care suggestion for today:")
print(random.choice(self_care_activities))
print("Remember, You're doing great!")
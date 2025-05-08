'''
Project Description
    Create a program that asks the user about the current weather and, using a dictionary for decision-making, suggests an activity.
    Start the script with this dictionary on top of your script:

    weather_activities = {
        "1": "It's a beautiful day! How about a walk in the park? 🌳",
        "2": "Perfect weather for a cozy indoor day with a good book! 📚",
        "3": "Maybe it's a great time for a reflective cup of tea! ☕",
        "4": "Build a snowman or have a snowball fight! ⛄"
    }
    Then, add more code so the program produces the following output.

Expected Output
    (1) The program prompts the user to choose 1, 2, 3, or 4 depending on the current weather.
    (2) Then, the program displays some text that belongs to the choice in the dictionary given further above.

Learning Benefits
    Dictionaries for Decision-Making:Practice using dictionaries to map inputs to outputs, reducing repetitive conditional statements.
'''

weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

print("what's the weather like today?")
print("\n1. sunny\n2. rainy\n3. cloudy\n4. snowy\n")
option=input("choose 1,2,3 or 4: ")

print(weather_activities[option])
print("\nstay safe and enjoy the weather!")
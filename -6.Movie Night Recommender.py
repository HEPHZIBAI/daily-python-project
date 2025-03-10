'''
Project Description
    Choosing a movie to watch can be a struggle, especially with so many options available. 
    In this project, you’ll create a simple Python program that suggests a random movie based on the genre the user selects. 
    The program will use a predefined dictionary of movies and genres, allowing users to get a quick recommendation without endless scrolling.

movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}

Expected Output
    The program displays some initial message (i.e., Welcome to the Movie Night…) and then prompts the user to enter a genre. 
    The user has entered “Drama” in the following example, so the program has selected a random movie from the “Drama” category (i.e., The Green Mile).
    If the user enters a genre that is not in our data, the progrma should return the message “❌ Sorry, that genre is not available. Try again!”

How This Project Matters in the Real-World
    This project introduces how data is stored and retrieved using dictionaries, which is a simplified way of working with structured data. 
    In real-world applications, movie recommendations are usually based on large databases that store movie details, genres, and user preferences. 
    When working with such databases, data is often retrieved in a structured format, such as a list of dictionaries in Python. 
    For example, a real database query might return something like this:

movies_from_db = [
    {"title": "Mad Max: Fury Road", "genre": "Action"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "Superbad", "genre": "Comedy"}
]
To process this data in Python, you typically convert it into a dictionary format, just like in this project. Understanding how to structure and manipulate dictionary-based data is a key skill when working with real databases in applications like movie streaming platforms, e-commerce product filtering, and online recommendation engines.

Prerequisites
    Required Libraries: datetime, random
'''
import random
print("welcome to the movie night recommender!")
print("available genres:Action,Comedy,Drama,Sci-Fi,Horror")
genres=input("enter a genre: ")

movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}
if genres in movies:
    print("you should watch:"+random.choice(movies[genres]))
else:
    print("sorry that genre is not available try again!")
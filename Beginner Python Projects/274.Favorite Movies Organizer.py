'''
Project Description
    Create a program that starts with a predefined list of your favorite movies. 
    For example:
        favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    Place the above list in your .py script and then add some code that does the following:
    Adds a new movie to the list (e.g., “Godfather”).
    Removes a specific movie from the list (e.g., “The Matrix”).
    Prints out the total number of movies in the list.
    Prints out the movies in alphabetical order.
    Here is how the output would look like after running the program:

Learning Benefits
    List Operations: Covers essential list methods like append(), remove(), len(), and sort().
    Real-Life Relevance: Organizing favorite items is a relatable and fun concept.
    Encourages Creativity: Students can modify the movie list with their own favorites.
    Looping Practice: Students practice iterating through lists and displaying results.

'''
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

favorite_movies.append("The Godfather")
favorite_movies.remove("The Matrix")
favorite_movies.sort()

print("Total number of movies:",len(favorite_movies))
print("Your favorite movies in alphabetical order:")

for i in favorite_movies:
    print("-",i)
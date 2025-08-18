'''
Project Brief
Your task for this project is to build a recipe API with Python and the Flask web framework.

Step-by-Step Instructions
Start your script by storing these sample recipe data as a variable:

recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}
Build an API using Flask that handles API GET requests for single recipes. For example, if the user visits (i.e., makes a GET request) http://127.0.0.1:5000/recipes/2 the recipe with ID 2 should load on the browser as JSON.

'''
'''
Project Description
    Create a simple meal planner that suggests balanced meals for breakfast, lunch, and dinner.

How the Program Works
    This program generates a random meal plan for breakfast, lunch, and dinner. There should be a different plan every time the user runs the program. This makes sure that over time there is a rich range of nutritious meals.
    Here is an example of the generated output when running the program:
    Any time we run the program, a different meal plan is generated:

Here is another run:
    Feel free to use these meals in your program:
    breakfast_options = ["Oatmeal with fruits", "Scrambled eggs and toast", "Smoothie bowl", "Greek yogurt with granola"]
    lunch_options = ["Grilled chicken salad", "Quinoa with roasted veggies", "Spaghetti with tomato sauce", "Sushi rolls"]
    dinner_options = ["Baked salmon with rice", "Vegetable stir-fry", "Chickpea curry", "Tacos with beans and avocado"]

How This Project Matters in the Real-World
    This project demonstrates how real-life meal planning apps work by randomly selecting meal options based on predefined lists. 
    In practice, similar logic is used in nutrition apps and meal delivery services to create customized meal plans for users. 
    Additionally, it introduces students to dictionary-based data storage and how real-world applications structure and retrieve information efficiently.

Prerequisites
    Required Libraries: random
'''
import random

print("welcome to the meal planner assistant!")
breakfast_options = ["Oatmeal with fruits", "Scrambled eggs and toast", "Smoothie bowl", "Greek yogurt with granola"]
lunch_options = ["Grilled chicken salad", "Quinoa with roasted veggies", "Spaghetti with tomato sauce", "Sushi rolls"]
dinner_options = ["Baked salmon with rice", "Vegetable stir-fry", "Chickpea curry", "Tacos with beans and avocado"]

print("breakfast :",random.choice(breakfast_options))
print("lunch :",random.choice(lunch_options))
print("dinner :",random.choice(dinner_options))

print("enjoy your meals and eat healthy")
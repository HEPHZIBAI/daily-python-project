'''
Project Description
	Create a program that suggests random workout routines based on user input, making fitness more 	engaging and personalized.

How the Program Works
	The program starts by letting the user enter a workout type. For example, in the demo below, the 	user has entered “strength”. Once the user presses Enter, the program selects a random exercise 	(i.e., planlk) from the strength category and prints out the messages as shown below:

	To make your work easier, we are providing 
		some strength exercises here:
		["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"]
		Some cardio exercises:
		["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"]
		some flexibility exercises:
		["Yoga Stretch", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"]

Prerequisites
	Required Libraries: random

'''

import random

strength = ["Push-ups", "Squats", "Lunges", "Plank", "Dumbbell Press"]
cardio = ["Jumping Jacks", "Burpees", "Running in Place", "Jump Rope", "High Knees"]
flexibility = ["Yoga Stretch", "Hamstring Stretch", "Toe Touches", "Cat-Cow Stretch", "Shoulder Rolls"]

print("welcome to the workout routine generator!")
choose=input("choose your workout type (cardio/strength/flexibility):")
if choose=="strength":
	print("try this exercise : ",random.choice(strength))
elif(choose=="cardio"):
	print("try this exercise : ",random.choice(cardio))
elif(choose=="flexibility"):
	print("try this exercise : ",random.choice(flexibility))
else:
	print("enter correct choice")

print("stay active and keep moving!")
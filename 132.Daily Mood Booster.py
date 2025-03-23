'''
Project Description
    Create a program that prompts the user to enter their mood (Happy, Stressed, or Tired) and 
    display a message depending on the moood submitted by the user.

Expected Output
    (1) The program prompts the user to enter their name (e.g., Ardit)
    (2) The program greets the user with “Hi. [name]! How are you feeling today? and displays the mood options.
    (3) The user chooses a number (1, 2, or 3).
    (4) If the user is happpy, the program displays “That’s great, [name]! Keep streading your joy“
    (5) If the user is stressed, the program displays “Take a deep breath, [name]. You're doing amazing!“
    (6) If the user is tired, the program displays “Rest up, [name]. Tomorrow is a fresh start!“

Learning Benefits
    Input Handling:
        You will practice getting user input and responding based on their choices.
    Conditional Statements:
        Learn how to use if-elif-else to make decisions in your program.
    String Manipulation:
        Practice combining strings to create personalized outputs dynamically.
'''

name=input("hello! what's your name? ").strip()

print(f"hi, {name}! how are you feeling today?")
print("1. happy\n2. stressed\n3. tired\n")

option=int(input("choose 1, 2 or 3: "))

if option==1:
    print(f"That’s great, {name}! Keep streading your joy")
if option==2:
    print(f"Take a deep breath, {name}. You're doing amazing!")
if option==3:
    print(f"Rest up, {name}. Tomorrow is a fresh start!")
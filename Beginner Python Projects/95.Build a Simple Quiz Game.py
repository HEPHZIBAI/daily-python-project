'''
Project Overview 💡
    In this project, you'll build a basic multiple-choice quiz game in the terminal. 
    You'll learn how to use functions, lists, conditionals, and user input to create an interactive experience.

Task:
    Write a Python program that:
    Stores a list of multiple-choice questions
    Asks each question and displays the options
    Takes the user’s input and checks if it’s correct
    Calculates and displays the final score

Expected Output:
    1. The program starts by providing the question and choices and asking the user to pick an answer (1, 2, 3, or 4):
    2. The user enters a number (e.g., 2). The program prints out “Correct! if the answer is correct:
    3. The program shows the second question (e.g., Which planet is known as the Red Planet?”). If the user enters a wrong answer, the program prints the relevant message. The process is repeated with a third question:
    4. Finally, the program prints out the total score to the user after three questions:

    To make your job easier, here are the data from the above quiz:
    
        quiz_questions = [("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1),]

Comparison
    The original version uses tuples and a clean, function-based design.
    The alternative version introduces shuffling and dictionary structures for more flexibility.

'''

quiz_questions = [("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),     
                  ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),     
                  ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1), ]

for i in quiz_questions:
    print(i[0])
    k=1
    for j in i[1]:
        print(k,".",j)
        k+=1
    o=int(input("your answer (1/2/3/4): "))
    if o==i[2]:
        print('correct!')
    else:
        print(f"wrong! the correct answer was {i[2]} {i[1][i[2]-1]}")
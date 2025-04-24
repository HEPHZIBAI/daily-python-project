'''
Project Description
    This project is about creating a program that runs on the terminal and lets the user store student names and their grades.

How the Project Works
    (1) Start the program by defining an empty dictionary on top of the Python script:
        grades = {}
    The program should get student names and grades from the user and update the grades dictionary (e.g., grades = {“John Smith“: “A+”, “Sarah Smith”: “B”})
    (2) To get the data from the user, the program prints out the instructions and prompts the user to choose an option, 1, 2, or 3:
    (3) If the user enters 1 that means they want to add a student and their grade. 
    Therefore, the program prompts the user to enter a student name (e.g., John Smith), and a grade (e.g., A):
    (4) Once the user submits the grade, the program should add that student-grade pair to the grades dictionary. 
    Then, the program lets the user know that the student and the grade were added. Then, the process is repeated to let the user add more student-grade pairs.
    If the user chooses option 2, the student and their grades should be printed out in the terminal. 
    If they choose 3, the program should exit.

'''

grades={}

choice=0

while True:
    print("\nMenu:\n1. add a student and their grade\n2. view all student and their grade\n3. exit\n")
    choice=int(input("choose an option (1 - 3) : "))
    if choice==1:
        name=input("enter the students name : ")
        grade=input(f"enter {name}'s grade : ")
        print(f"{name}'s grade has been added.")
        grades[name]=grade  
    elif choice==2:
        for i,j in grades.items():
            print(i,j)
    else:
        break
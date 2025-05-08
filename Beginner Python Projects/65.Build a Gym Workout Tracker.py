'''
Project Description
    This program helps you track your workout routines, sets, reps, and weights. 
    It lets you add exercises, record your progress, and review past workouts. 
    Perfect for gym users who want to log their progress.

How the project works
    The program is command line based and it starts by letting the user choose any of the options.
    At first, the user may want to add an exercise type. Here the user adds a pushup and a squat exercise:
    Once the user has added a few exercise types, they can log an exercise whenever they perform that exercise. 
    Here the user has logged in the pushups exercise, declaring 3 sets of 10 reps each and 0 as extra weight.
    Finally, the user see their progress by choosing option 3. View Progress:
    As you can see in the last line, the program shows that the user has done a session and it displays the details about that session.
    You can use procedural or functional programming to code this project, but we used object-oriented programming in the solution in the “Show Code” button. 
    For simplicity, we are not saving the user data in any files, but simply inside the program temporarily.
'''
class gym:
    def __init__(self):
        self.exercises={}

    def add(self):
        exercise=input("Enter exercise name: ").strip()
        if exercise not in self.exercises:
            self.exercises[exercise]=[]
        #self.exercises[exercise].append({'sets':0,'reps':0,'kg':0})
        print("Added exercise:",exercise)

    def log(self):
        exercise=input("Enter exercise name: ").strip()
        sets=int(input("Enter number of sets: "))
        reps=int(input("Enter number of reps: "))
        weight=float(input("Enter weight in kg: "))
        if exercise not in self.exercises:
            self.exercises[exercise]=[]
        self.exercises[exercise].append({'sets':sets,'reps':reps,'kg':weight})
        print(f"Logged {sets} sets of {reps} reps at {weight} kg for pushups")

    def progress(self):
        h=list(self.exercises.keys())
        for i in h:
            k=1
            print(f"progress for {i}:")
            for j in self.exercises[i]:
                print(f"Session {k}: {j['sets']} sets of {j['reps']} reps at {j['kg']} kg")
                k+=1

gexercise=gym()
choice=0
while choice!=4:
    print("Gym Tracker Options:\n1. Add Exercise\n2. Log Workout\n3. View Progress\n4. Exit")
    choice=int(input("Choose an option: "))
    if choice==1:
        gexercise.add()
    elif choice==2:
        gexercise.log()
    elif choice==3:
        gexercise.progress()
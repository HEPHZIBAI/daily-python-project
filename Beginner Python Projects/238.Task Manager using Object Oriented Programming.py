'''
Project Description
    Create a console-based task manager app where users can add, complete, and view tasks.

How the Project Works
    When the program runs, the user is prompted to choose one of the options (add, complete, view task, or exit the program). 
    If the user chooses to add a task, they submit “1” and then type in the task. 
    The user can also view the tasks. 
    Tasks that are not completed are shown with an ❌ next to them. 
    After the user completes a task, a ✔️ is shown next to the task when the user views the tasks.
    Please use OOP/classes to build the program. 
    Below is a structure to get you started and in the “Show Code” button you will find the complete solution.

class Task:     
    def __init__(self, description):         
        self.description = description         
        self.is_completed = False      
    def mark_completed(self):         
        self.is_completed = True         
        ...  
        
class ToDoList:     
    def __init__(self):         
        self.tasks = []      
    def add_task(self):         
        description = input("Enter the task description: ")         
        ...      
    def complete_task(self):         
        self.view_tasks()         
        ...      
    def view_tasks(self):         
        ...     
    def run(self):         
        ...  
if __name__ == "__main__":    
    todo_list = ToDoList()     
    todo_list.run()  

You can save the tasks in variables instead of external files/databases to keep the solution simple.
'''

class Task:     
    def __init__(self, description):         
        self.description = description         
        self.is_completed = '❌'      
    def mark_completed(self):         
        self.is_completed = '✔️'          
        
class ToDoList:     
    def __init__(self):         
        self.tasks = [] 

    def add_task(self):         
        description = input("Enter the task description: ")
        self.tasks.append(Task(description))        
        print(f"task \'{description}\' added to the to-do list.")

    def complete_task(self):         
        self.view_tasks() 
        task=int(input("enter the task number to mark as completed: ")) 
        task-=1
        j=0
        des=""
        i=''
        for i in self.tasks:
            if j==task:
                des=i.description
                break
            j+=1
        
        i.mark_completed()
        print(f"task \'{des}\' marked as completed.")       
          
    def view_tasks(self):  
        j=1       
        for i in self.tasks:
            print(f"{j}. {i.description}. [{i.is_completed}]")
            j+=1
 

todo_list = ToDoList()     

option=0

while option!=4:
    print("1. add task\n2. complete task\n3. view tasks\n4. exit")
    option=int(input("enter choice: "))
    if option==1:
        todo_list.add_task()
    elif option==2:
        todo_list.complete_task()
    elif option==3:
        todo_list.view_tasks()

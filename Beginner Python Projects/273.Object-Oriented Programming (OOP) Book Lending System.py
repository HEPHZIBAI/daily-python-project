'''
Project Description
    For today’s project, the task is to build a console-based book lending system for a small library or a personal book collection. 
    This app allows users to browse available books, borrow a book, return a book, and view all borrowed books.
    The user can choose option 1 to view available books for borrowing:
    The user can choose 2 and then enter the number of the book they want to borrow:
    The user can choose 3 to return a book so the book becomes available again for borrowing:

    👉 We challenge you to use classes (i.e., OOP) instead of functions this time. Here is how the code would look like. You can complete the rest yourself.

    class BookLendingSystem:     
        def __init__(self):         
            self.available_books = {1: "The Great Gatsby",2: "To Kill a Mockingbird",3: "1984",4: "Pride and Prejudice"}
            self.borrowed_books = {}  

        def display_menu(self):         
            print("\nWelcome to the Book Lending System!")
            ...
            ...       
        
        def view_available_books(self):         
            ...         
            ...      
            
        def borrow_book(self):         
            if not self.available_books:             
                ...             
                ...      
                
        def return_book(self):         
            if not self.borrowed_books:             
                ...             
                ...      
                
        def view_borrowed_books(self):         
            if not self.borrowed_books:             
                ...             
                ...      
        def run(self):         
            while True:             
                self.display_menu()             
                choice = input("\nChoose an option: ").strip()             
                if choice == "1":                 
                    ...                 
                    ...                   
    system = BookLendingSystem() 
    system.run()   

Learning Benefits
    You will practice managing lists and dictionaries, 
    handling user input, and 
    implementing logical workflows for an interactive application. 
    In addition, you will practice working with classes.
'''
class books:
    def __init__(self):
        self.available_books = {1: "The Great Gatsby",2: "To Kill a Mockingbird",3: "1984",4: "Pride and Prejudice"}
        self.borrowed_books = {} 

    def show(self):
        print("\n---Available books---")
        for i in list(self.available_books.keys()):
            print(i,'.',self.available_books[i])
        print()

    def borrow(self):
        self.show()
        number=int(input("enter the book numver to borrow:"))
        name=input("enter your name:")
        self.borrowed_books[number]=[self.available_books[number],name]
        print(f"you have borrowed \"{self.available_books[number]}\".please return it on time.")
        self.available_books.pop(number)

    def returnbook(self):
        self.view()
        number=int(input("enter the book number to return :"))
        print(f"thank you, {self.borrowed_books[number][1]} , for returning \"{self.borrowed_books[number][0]}\"")
        self.available_books[number]=self.borrowed_books[number][0]
        self.borrowed_books.pop(number)

    def view(self):
        print("--borrowed books--")
        for i in list(self.borrowed_books.keys()):
            print(f"{i}. {self.borrowed_books[i][0]} - {self.borrowed_books[i][1]}")



book=books()
option=0

while option!=5:
    print("welcome to the book lending system!\n")
    print("1. view available books\n2. borrow a book\n3. return a book\n4. view borrowed books\n5. exit\n")
    
    option=int(input("choose an option: "))
    
    if option==1:
        book.show()
    if option==2:
        book.borrow()
    if option==3:
        book.returnbook()
    if option==4:
        book.view()
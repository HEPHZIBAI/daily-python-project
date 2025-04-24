'''
Project Description
    Create a console-based library management system where users can:
    Add books
    Borrow books
    Return books
    View available books
    Exit the system

How the Project Works
    The screenshot below shows how the program works. 
    The user adds a book (title), views the books, borrows a book, and views again the available books. 
    When a book is borrowed, it is not in the list of available books anymore.
    Please use OOP/classes to build the program. 
    Below is a structure to get you started and in the “Show Code” button you will find the complete solution.

    class Book:     
        def __init__(self, title):         
            self.title = title         
            self.is_available = True      
        
        def mark_as_borrowed(self):         
            if self.is_available:             
                ...         
            else:             
                print(f"Sorry, '{self.title}' is currently not available")      
        
        def mark_as_returned(self):         
            self.is_available = True         
            ...   
            
    class Library:     
        def __init__(self):         
            self.books = []      
            
        def add_book(self):         
            title = input("Enter the title of the book: ")         
            ...      
            
        def borrow_book(self):         
            ...      
            
        def return_book(self):         
            ...      
            
        def view_books(self):         
            ...      
            
        def run(self):         
            while True:             
                print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. View Available Books\n5. Exit")             
                choice = input("Enter choice: ")              
                if choice == '1':                 
                    self.add_book()             
                elif choice == '2':                 
                    ...  
                    if __name__ == "__main__":     
                        library = Library()     
                        library.run()
        
    You can save the data (i.e., accounts, deposits, etc) in variables instead of external files/databases to keep the solution simple.

'''

class Book:     
    def __init__(self, title):         
        self.title = title         
        self.is_available = True      
        
    def mark_as_borrowed(self):         
        if self.is_available:             
            self.is_available=False
            print(f"yor have borrowed '{self.title}'")         
        else:             
            print(f"Sorry, '{self.title}' is currently not available")      
        
    def mark_as_returned(self):         
        self.is_available = True    
        print(f"yor have returned '{self.title}'")       
            
class Library:     
    def __init__(self):         
        self.books = []      
            
    def add_book(self):         
        title = input("Enter the title of the book: ")         
        print(f"'{title}' has been added to the library")    
        self.books.append(Book(title)) 

    def borrow_book(self):         
        title=input("Enter the title of the book to borrow: ").strip()
        for i in self.books:
            if i.title==title:
                i.mark_as_borrowed()     
            
    def return_book(self): 
        title=input("Enter the title of the book to return: ").strip()        
        for i in self.books:
            if i.title==title:
                i.mark_as_returned()
            
    def view_books(self):  
        print("available books:")
        m=0
        for i in self.books:
            if i.is_available:
                print("-",i.title)
                m=1
        if m==0:
            print("no books available right now.")
         
library=Library()          
while True:             
    print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. View Available Books\n5. Exit")             
    choice = int(input("Enter choice: "))           
    if choice==1:
        library.add_book()
    elif choice==2:
        library.borrow_book()
    elif choice==3:
        library.return_book()
    elif choice==4:
        library.view_books()
    else:
        break
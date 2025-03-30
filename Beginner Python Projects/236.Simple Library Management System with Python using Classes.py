'''
Project Description
Create a console-based library management system where users can:

Add books

Borrow books

Return books

View available books

Exit the system

How the Project Works
The screenshot below shows how the program works. The user adds a book (title), views the books, borrows a book, and views again the available books. When a book is borrowed, it is not in the list of available books anymore.


Please use OOP/classes to build the program. Below is a structure to get you started and in the “Show Code” button you will find the complete solution.

class Book:     def __init__(self, title):         self.title = title         self.is_available = True      def mark_as_borrowed(self):         if self.is_available:             ...         else:             print(f"Sorry, '{self.title}' is currently not available")      def mark_as_returned(self):         self.is_available = True         ...   class Library:     def __init__(self):         self.books = []      def add_book(self):         title = input("Enter the title of the book: ")         ...      def borrow_book(self):         ...      def return_book(self):         ...      def view_books(self):         ...      def run(self):         while True:             print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. View Available Books\n5. Exit")             choice = input("Enter choice: ")              if choice == '1':                 self.add_book()             elif choice == '2':                 ...  if __name__ == "__main__":     library = Library()     library.run()
You can save the data (i.e., accounts, deposits, etc) in variables instead of external files/databases to keep the solution simple.

Prerequisites'''


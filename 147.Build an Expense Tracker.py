'''
Project Description
    Create a command-line app to track daily expenses. 
    The app allows users to add expenses, view a summary of all expenses, and calculate total spending for a given period. 
    It's great for practicing file handling, date manipulation, and list/dictionary management.
    Here is what the app does exactly:
    Add Expense: Input the date, category, description, and amount.
    View All Expenses: Display all recorded expenses in a neat tabular format
    Search Expenses by Date: View expenses for a specific date or range of dates.
    Calculate Total Spending: Show the total amount spent across all categories
    Save and Load Data: Save expense records to a file and load them on app start.

Learning Benefits
    You will enhance your understanding of file handling, working with dates, and organizing data using Python dictionaries and lists.

Prerequisites
    Required Libraries: os, datetime
'''
import pandas as pd

class expense:
    def __init__(self):
        self.f=pd.read_csv('147.Build an Expense Tracker.csv')
        print(self.f.head())

    def add(self):
        date=input("enter date (yyyy-mm-dd): ")
        category=input("enter category: ")
        description=input("enter description: ")
        amount=float(input("enter amount:"))
        
        print("expense added successfully!")

option=0
expenses=expense()

while option!=5:
    print("welcome to the expense tracker!\n")
    print("1. add an expense\n2. view all expenses\n3. search expenses by date\n4. calculate total spending\n5. exit\n")
    option=int(input("choose an option: "))
    if option==1:
        expenses.add()
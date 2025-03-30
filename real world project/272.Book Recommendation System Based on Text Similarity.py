'''
Project Description
    Today we build a program that suggests books to users based on the similarity of their plot summaries.

Expected Output
    The program lets the user provide a plot summary of a book they enjoyed in the terminal. 
    This user here liked the “Evolution’s Captain” book:
    Then, the app recommends the top 5 similar books:
    This project involves natural language processing and text similarity analysis. 
    The books suggested by the program are taken from this CSV file which contains book titles and their summaries:

Prerequisites
    Required Libraries: pandas, scikit-learn
                        pip install pandas scikit-learn
    Required Files: Download the book.csv file that contains book titles and summaries.
'''

description=input("enter a brief plot summary of a book you like:\n")
print("recommended books:")
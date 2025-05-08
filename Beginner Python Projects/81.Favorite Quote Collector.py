'''
Project Description
    Your task for today’s project is to create a Python program that allows users to add their favorite quotes to a text file and 
    then display all saved quotes.

How the Program Works
    The program starts by asking the user to enter a quote:
    For example, the user types in a quote from Franklin D. Roosevelt, and the program saves it in a quotes.txt file, and 
    prints out all the saved quotes.

How This Project Matters in the Real-World
    Storing and retrieving text-based information is a core function in many applications. 
    This simple program mirrors how user-generated content, such as notes, journal entries, or testimonials, is saved and 
    displayed in real-world apps like note-taking tools, blogging platforms, or personal databases.

'''
f=open("./Biginner Python Projects/81.Favorite Quote Collector.txt",'a')
quote=input("enter your favorite quote : ")
f.write("\n"+quote)
print("Quote saved!")
print("all saved qutes")
f=open("./Biginner Python Projects/81.Favorite Quote Collector.txt",'r')
k=f.readlines()
j=1
for i in k:
    print(j,'.',i,end="")
    j+=1
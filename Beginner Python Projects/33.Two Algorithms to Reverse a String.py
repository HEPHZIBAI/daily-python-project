'''
Project Description
    Your task for today is to write some code that reverses any string. 
    There are two fundamentally different ways to accomplish this, one using a for-loop and another using string slicing. 
    If you can, write both solutions.

How the Project Works
    Start your script by defining a sentence as a string. 
    Here is an example:
        text = "Python is fun!"
    Here is how the program behaves when run:
'''

text = "Python is fun!"

print("the reversed string is:",text[::-1])
print("the reversed string is:",end=" ")
      
for i in range(-1,-len(text)-1,-1):
    print(text[i],end="")
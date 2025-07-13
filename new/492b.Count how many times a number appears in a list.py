'''
Project Description
    Your task for today is to build a Python program that counts how many times a specific number appears in a list. 
    But instead of using a pre-defined list, your program should ask the user to enter the list and the target number via the terminal.
    The user will type in the list as comma-separated numbers, like 3, 4, 5, 3, 2, 3, and your program should process that input and determine how many times their chosen number appears.
    This kind of number-counting logic is used in many real-world situations: from analyzing how many times a value appears in survey responses, to counting specific occurrences in datasets or log files. 
    Learning how to clean and process user input will serve you well in any kind of data-focused project.

Expected Output
    The program should prompt the user twice:
'''

a=list(map(int,input("enter a list of numbers separated by commas: ").split(",")))
num=int(input("enter the number you want to count: "))
k=0

for i in a:
    if i==num:
        k+=1

print(f"the number {num} appears {k} times in the list.")
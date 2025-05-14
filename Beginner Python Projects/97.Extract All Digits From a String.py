'''
Project Description
    Your task for today is to write a Python program that extracts all the digits from a given string and stores them in a list.
    Start with a string stored in a variable. For example:
        text = "The year is 2025 and the time is 09:45."
    Your program should scan this string character by character and collect all the digits.

Expected Output
    The program should print out a list containing only the digits from the string. For example:
    ['2', '0', '2', '5', '0', '9', '4', '5']
'''


text = "The year is 2025 and the time is 09:45."
a=[]

for i in text:
    if i>='0' and i<='9':
        a.append(i)

print(a)
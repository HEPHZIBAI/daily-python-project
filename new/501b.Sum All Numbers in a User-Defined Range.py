'''
Project Description
    Your task for today is to build a Python program that calculates the sum of all numbers in a user-defined range. 
    Instead of hardcoding the start and end values, your program will prompt the user to enter them.
    You’ll then write a function that loops through each number from the start to the end (inclusive) and calculates the total sum. 
    This is a super practical beginner project — you’ll see similar logic in billing systems (summing prices from one invoice to another), generating statistics over days or months, or even calculating cumulative points in a game.

Expected Output
    When you run the program, it should look like this:
    It adds up 3 + 4 + 5 + 6 + 7 + 8 and prints the total.
'''

start=int(input("enter the start of the range: "))
end=int(input("enter the end of the range: "))
sum=0

for i in range(start,end+1):
    sum+=i

print(f"the sum of all numbers from {start} to {end} is: {sum}")
'''
Your task for today is to build a Grade Calculator that processes a list of scores using functions. 
This project will help you practice defining and calling functions, handling input validation, and formatting results in a clear way.

📝 Project Task
    The program should:
        Define a function that takes a list of scores and returns:
            The average score (rounded to 2 decimals).
            The letter grade (A, B, C, D, F).
            Whether the student passed or failed (e.g., pass if ≥ 60).
        Prompt the user to enter multiple scores separated by commas.
        Validate input (only allow numeric values between 0 and 100).
        Print results in a formatted style.
    
    Bonus (optional):
        Support multiple students by repeating the input prompt in a loop.
        Save results to a text or CSV file.
    This project strengthens your skills with functions, conditional logic, and user input validation.

📌 Expected Output
When run, the program should behave like this:
If the input is invalid:
'''
result=''
a=list(map(int,input("enter scores separated by commas: ").split(',')))
average=round(sum(a)/len(a),2)
print("average: ",average)
grade=''
if average>=90:
    grade='A'
elif average>=80:
    grade='B'
elif average>=70:
    grade='C'
elif average>=60:
    grade='D'
else:
    grade='F'
if average>=60:
    result="Pass"
else:
    result="Fail"
print("letter grade: ",grade)
print("result: ",result)
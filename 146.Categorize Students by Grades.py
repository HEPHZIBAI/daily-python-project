'''
Project Description
    For this project, your task is to perform some categorization of dictionary data. 
    Create a .py script and paste the following dictionary there. 
    The dictionary contains student grades.

    grades = {
        "Alice": 78,
        "Bob": 42,
        "Charlie": 65,
        "Diana": 49,
        "Eve": 90
    }
    Add some code after the above dictionary. The code should create a new dictionary that categorizes students into "Pass" or "Fail" based on their grades. Consider a grade of 50 or higher as "Pass" and below 50 as "Fail." Once you create a dictionary, use a for-loop to iterate over the new dictionary and print out each pair of key and value as below:

Learning Benefits
    Dictionary Creation: Introduces creating new dictionaries from existing ones.
    Conditional Logic: Reinforces the use of if-else statements for decision-making.
    Practical Use Case: Models a real-world scenario of evaluating and categorizing data.
'''
grades = {
    "Alice": 78,
    "Bob": 42,
    "Charlie": 65,
    "Diana": 49,
    "Eve": 90
}

grade={}
print("student categories:")
for i in list(grades.keys()):
    if grades[i]>=50:
        grade[i]="pass"
    else:
        grade[i]="fail"

    print(i,":",grade[i])
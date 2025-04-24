'''
Project Description
    Create a command-line calculator that performs basic mathematical operations such as:
        Addition
        Subtraction
        Multiplication
        Division
        Power (exponentiation)

How the Project Works
    As shown above, the program prompts the user to enter an expression (e.g., 6 + 5). 
    Once the user enters the expression and presses Enter, the program shows the result (i.e., 11). 
    Then, the program prompts the user again to enter another expression. 
    This loop continues until the user enters “exit” to exit the program.
'''

print("text-based calculator")
print("enter a mathematical expression (e.g., 5 + 3) or type 'exit' to quit.")
expression=""

while expression!='exit':
    expression=input("enter expression: ").strip()
    print('result')
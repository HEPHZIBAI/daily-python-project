'''
Project Description
    Create a simplified ATM Simulation program where the user interacts with an ATM-like interface through the command line. 
    The user can perform basic transactions, such as checking their balance, depositing money, and withdrawing money.

    Here is how the program works:
        (1) The program starts with a default balance of $100 and displays the options (e.g., check balance, deposit, etc.)
        (2) The user chooses an option number (e.g., 3 for depositing) and then follows the instructions (e.g., enters a deposit amount).
        (3) The program calculates the updated balance and prints out the messages again and the updated balance.

Learning Benefits
    This project helps beginners understand the fundamentals of conditional statements and loops in Python by simulating real-life decision-making processes. 
    The program can also optionally include basic error handling. 
    Additionally, users gain insight into managing and updating variables dynamically based on user actions.
'''

print("welcome to the atm!")

option=0
current=100

while option!=3:
    print("\ncurrent balance: $",current)
    print("1. deposit money\n2. withdraw money\n3. exit\n")
    option=int(input("choose an option: "))
    
    if option==1:
        amount=int(input("enter amount to deposit: "))
        current+=amount
        print("deposit sussessful! your new balance is: ",current)
    elif option==2:
        amount=int(input("enter amount to withdraw: "))

        if amount>current:
            print("your balance is low")
        else:
            current-=amount
            print("withdrawal successful! your new balance is: $",current)
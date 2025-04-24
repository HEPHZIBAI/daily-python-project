'''
Project Description
    Create a basic console-based banking system where users can:
        Create accounts
        Deposit money
        View balance
        Exit the system.

How the Project Works
    The screenshot below shows how the program works. 
    The user creates an account, deposits money, views the balance, and exits:
    Consider using OOP/classes to build the program. 
    Below is a structure to get you started and in the “Show Code” button you will find the complete solution.

class Account:     
    def __init__(self, name, initial_deposit):         
        self.name = name         
        self.balance = initial_deposit      
    def deposit(self, amount):         
        ...      
    def view_balance(self):         
        ...   
        
class BankSystem:     
    def __init__(self):         
        self.accounts = {}      
    def create_account(self):         
        ...      
    def deposit_money(self):         
        ...      
    def view_balance(self):         
        ...      
    def run(self):         
        while True:             
            print("\n1. Create Account\n2. Deposit Money\n3. View Balance\n4. Exit")             
            choice = input("Enter choice: ")              
            if choice == '1':                 
                ...  
            if __name__ == "__main__":     
                bank_system = BankSystem()     
                bank_system.run()

To keep it simple, just save the data (i.e., accounts, deposits, etc) in variables instead of external files/databases.

Prerequisites
    Required Libraries: No libraries are required.
    Required Files: No files are required.
    IDE: You can use any IDE on your computer to code the project.
'''


class Account:     
    def __init__(self, name, initial_deposit):         
        self.name = name         
        self.balance = initial_deposit      
        
class BankSystem:     
    def __init__(self):         
        self.accounts = {}      
    def create_account(self):         
        name=input("enter your name: ").strip()
        deposit=float(input("enter initial deposit: "))
        self.accounts[name]=Account(name,deposit)
        print(f"account created for {name} with balance {deposit}")    
    def deposit_money(self):         
        name=input("enter your name: ").strip()
        deposit=float(input("enter amount to deposit: ")) 
        self.accounts[name].balance+=deposit
        print(f"{deposit} deposited. new balance: {self.accounts[name].balance}")   
    def view_balance(self):         
        name=input("enter your name: ").strip()
        print(f"account holder: {self.accounts[name].name} , balance: {self.accounts[name].balance}")      

choice=0
bank=BankSystem()

while choice!=4:
    print("1. create account\n2. deposit money\n3. view balance\n4. exit")
    choice=int(input("enter your choice: "))

    if choice==1:
        bank.create_account()
    if choice==2:
        bank.deposit_money()
    if choice==3:
        bank.view_balance()
    if choice==4:
        print("exiting...")
        break
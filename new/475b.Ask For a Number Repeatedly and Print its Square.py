'''
Project Description
    Your task for today is to write a Python program that repeatedly asks the user to enter a number and prints its square. 
    The program should keep running until the user types "q" to quit.
    This kind of loop is commonly used in real-world apps that continuously take user input, such as calculators or command-line tools.

Expected Output
    The program should work like this:
    As you can see, the program asks the user to enter a number. 
    The user enters “4” and the program prints out the message “Square: 16”. 
    The user can continue to enter numbers, but if they enter “q” the program should quit.
'''

while True:
    a=input("enter a number (or 'q' to quit) : ")
    
    if a=='q':
        break
    
    print("square: ",int(a)*int(a))
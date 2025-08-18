'''
Your task for today is to write a Python program that simulates a basic login system with a limited number of attempts. 
This project will help you practice while loops, conditional logic, and handling repeated user input.

📝 Project Task
    The program should:
        Let the user attempt to enter a password.
        Give them up to 3 tries using a while loop.
        If the user enters the correct password within 3 tries, print a success message like "Access granted."
        If the user fails 3 times, print "Too many attempts. You are locked out."

    You can hardcode the correct password as "python123" for this exercise.

📌 Expected Output
    If the user succeeds:
        Enter password: hello
        Incorrect password. Try again.
        Enter password: python123
        Access granted.
    If the user fails all 3 attempts:
        Enter password: test
        Incorrect password. Try again.
        Enter password: admin
        Incorrect password. Try again.
        Enter password: letmein
        Too many attempts. You are locked out.
    This project is a great stepping stone toward building full authentication systems.
'''

password="python123"
i=0
for i in range(3):
    user=input("enter password : ").strip()
    if user==password:
        print("access granted")
        break
    else:
        print("incorrect password. try again.")
if i==3:
    print("Too many attempts.you ate locked out.")

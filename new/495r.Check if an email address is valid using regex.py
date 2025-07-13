'''
Project Description
    Your task today is to build a Python program that checks if an email address is valid — using regular expressions (regex). 
    This isn’t just a theoretical exercise: validating email formats is a real-world necessity for login systems, signup forms, newsletter signups, admin dashboards, and more.

Here’s the challenge:
    Ask the user to input an email address.
    Use a regular expression to validate if it has the correct format (like someone@example.com).
    Print whether it’s valid or not.
    And for those ready for an extra challenge:
    💡 Turn this into a small graphical app using tkinter, so users can paste an email and press a button to validate it.

This project gives you practice with:
    re.match() from Python’s re module
    Real-world string patterns and data validation
    Optional: building a tiny GUI with tkinter

Expected Output

'''

import re

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
email = input("Enter an email to check if it's valid: ").strip()

if re.match(email_pattern, email):
    print("✅ That's a valid email address!")
else:
    print("❌ That's not a valid email address!")

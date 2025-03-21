'''
Project Description
    Build a command-line application that evaluates the strength of a password entered by the user. 
    The app will analyze the password based on these criteria:

    Length (at least 8 characters long)
    The inclusion of uppercase and lowercase letters, numbers, special characters (using the re regular expression library)
    Dictionary word detection (the program uses the nltk library to detect if the user is using any common English words and it will not accept such words to make the password more secure).
    Here is an example when the user submits a weak password (e.g., mypass):
    As you can see the program also prints out some recommendations to provide a strong password.
    And here is an example of a strong password:

Learning Benefits
    Learn how to use Python’s re module for pattern matching.
    Gain insights into file operations by loading common password dictionaries using the word corpus from the nltk library.
    Understand how to provide user feedback and enhance usability.
    Develop experience with validating and analyzing strings for real-world scenarios.

Prerequisites
    Required Libraries: string, re, nltk
                        pip install nltk
'''

import re
import string
import nltk
from nltk.corpus import words

nltk.download("words")
word_list = set(words.words())

print("welcome to the password strength checker!")
password=input("enter your password: ").strip()


strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(rf"[{re.escape(string.punctuation)}]", password)),
        "dictionary_word": password.lower() not in word_list
    }

passed_criteria = sum(strength_criteria.values())

if passed_criteria == 6:
    print("Strong Password ✅")
else:
    suggestions = []
    
    if not strength_criteria["length"]:
        suggestions.append("Make your password at least 8 characters long.")
    
    if not strength_criteria["uppercase"]:
        suggestions.append("Include at least one uppercase letter.")
        
    if not strength_criteria["lowercase"]:
        suggestions.append("Include at least one lowercase letter.")
        
    if not strength_criteria["digit"]:
        suggestions.append("Include at least one number.")
    
    if not strength_criteria["special_char"]:
        suggestions.append("Include at least one special character.")
    if not strength_criteria["dictionary_word"]:
        suggestions.append("Avoid using common dictionary words.")

    print(f"Weak Password ❌\nRecommendations:\n- " + "\n- ".join(suggestions))
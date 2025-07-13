'''
Project Description
    Your task for today is to write a Python program that converts text into Morse code.
    Morse code is a method used in telecommunication to encode text characters using sequences of dots (.) and dashes (-). 
    For example, the letter A is written as .- and B is -.... Words are separated by slashes (/), and letters are separated by spaces.
    Your program will take a string as input (e.g., a sentence typed by the user), and output the Morse code version of that text. 
    You’ll use a dictionary to map letters and digits to their Morse equivalents.
    This project is a fun way to get comfortable with:
        Dictionaries
        String manipulation
        Loops
        Input/output
        Conditional logic
    It also shows how text transformation is done in real-world applications like encoding systems, secret messages, and simple cryptography.

Expected Output
    If the user enters:
        hello world
    The program should output:
        .... . .-.. .-.. --- / .-- --- .-. .-.. -..
'''


morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}


text=input("enter the word : ").strip().upper()

for i in text:
    if i in morse_code_dict:
        print(morse_code_dict[i],end="")
    else:
        print(i,end="")
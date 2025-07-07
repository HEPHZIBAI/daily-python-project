'''
Project Description
    Your project for today is to build a basic version of the classic Hangman game in Python.
    The program will choose a single secret word (hardcoded for now), and let the user guess one letter at a time. 
    After each guess, it will show the user their progress by revealing correctly guessed letters and keeping underscores (_) for letters they haven’t guessed yet.
    The user will have a limited number of incorrect guesses (like 6 tries). 
    If they guess all the letters before running out of tries, they win. 
    Otherwise, they lose and the word is revealed.

This is a perfect beginner project to learn about:
    Loops and conditionals
    Keeping track of state with lists (letters guessed so far)
    String building (showing progress with underscores)
    Plus it’s a fun game you can expand later by choosing words randomly from a list or even drawing ASCII hangman graphics.

Expected Output
    If they win:
    Or if they lose:
'''

w1="______"
ans="blacky"
n=6

while n>0 and w1!=ans:
    print("word: ",w1)
    ch=input("guss a letter: ").strip()
    if len(ch)!=1:
        print("one character at a time is allowed")
        continue
    if ch in ans:
        print("good guess!")
        for i in range(len(w1)):
            if ans[i]==ch:
                w1=w1[:i]+ch+w1[i+1:]
    else:
        print("wrong guess.")
        n-=1

if w1==ans:
    print("congratulations! you guessed the word: ",ans)
else:
    print("sorry, you ran out of tries.\nthe word was: ",ans)

print(w1)
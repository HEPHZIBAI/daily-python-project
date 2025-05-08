'''
Project Overview 💡
    In this project, you'll write a Python script that asks the user to enter three sentences and saves them into a text file. 
    Between each sentence (except the last), a dashed line will be written to visually separate them.

Task:
    Write a Python program that:
    Prompts the user to enter three different sentences
    Writes each sentence to a file, separated by a dashed line (-----------) except after the last one
    Saves the content to a file named user_sentences.txt

Expected Output:
    The program prompts the user three times to enter three sentences.
    Once the user has entered the three sentences, the program produces a text file with the three sentences inside and dashes between them.

Comparison
    The original version writes to the file as the user types.
    The alternative version collects all input first, which can make the logic easier to manage for more complex input tasks.

'''
sen1=input("enter sentence 1: ")
sen2=input("enter sentence 2: ")
sen3=input("enter sentence 3: ")

with open("./Beginner Python Projects/94.Save User Sentences to a File.txt",'a') as f:
    f.write(sen1+"\n")
    f.write("----------\n")
    f.write(sen2+"\n")
    f.write("----------\n")
    f.write(sen3+"\n")

print("sentences have been saved")
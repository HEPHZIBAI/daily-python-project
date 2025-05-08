'''
Project Description
    For this project, you are provided with the following messy list of strings that represent names:

    messy_names = ["  alice ", "Bob", " charlie", "Alice", "BOB ", "eve  ", " Eve", "eve"]

    Please place that list on top of your Python script. 
    As you can see, some names are in lowercase letters, some have extra spaces, and others are duplicates.
    Write a program that cleans the data by removing extra spaces, converting all names to title case, and removing any duplicates. 
    Finally, display the cleaned list in alphabetical order.

Expected Output
    Your task is to write a program that cleans the data by removing extra spaces, converting all names to title case (e.g., Alice), and removing any duplicates. 
    Finally, display the cleaned list in alphabetical order.
    Here is what the output of your program should be:

Why This Project Matters in the Real World
    This beginner-friendly example of cleaning up a list of names introduces you to a process that's crucial in many real-world applications. 
    For example, in cybersecurity, you might work with a list of IP addresses and need to remove duplicates before running a network scan. 
    Similarly, in software development, you may need to clean user inputs from a form, such as email addresses or file paths, to ensure the data is ready for processing. 
    For instance, in Python, cleaning file paths might look like this:

    file_paths = ["C:\\temp\\file1.txt", "C:\\temp\\file1.txt", "D:\\data\\file2.txt"]
    cleaned_paths = list(set(file_paths))
    This example mirrors the concepts you’ve just practiced but applies them to more practical scenarios, 
    showing how foundational skills like these can be the building blocks for solving real-world problems.
'''

messy_names = ["  alice ", "Bob", " charlie", "Alice", "BOB ", "eve  ", " Eve", "eve"]
for i in range(len(messy_names)):
    messy_names[i]=messy_names[i].strip()
    messy_names[i]=messy_names[i].title()

messy_names=list(set(messy_names))
messy_names.sort()

print("cleaned and sorted names:")
for i in messy_names:
    print(i)
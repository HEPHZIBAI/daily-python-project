'''
Your task for today is to write a Python script that loops through all files in a folder and renames them using a consistent naming pattern. This type of task is incredibly useful when organizing photos, documents, or any files with inconsistent names. You’ll get to practice working with Python’s os module and learn how to manipulate files programmatically.

📝 Project Task
The program should:

Use os.listdir() to get all files in a folder.

Loop through each file and rename it using os.rename().

Apply a naming pattern like file1.txt, file2.txt, etc.

Bonus: Let the user specify the folder and the filename prefix (e.g., document1.txt, document2.txt, etc.).

This kind of automation saves time and reduces manual errors when handling many files.

📌 Expected Output
If your folder contains:

IMG_001.png
random_photo.png
note.txt
After running the script, the folder will contain:

file1.png
file2.png
file3.txt
The numbering should continue through all files, and file extensions should be preserved.

'''
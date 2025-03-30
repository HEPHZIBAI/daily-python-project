'''
Project Objective
    Create a Python script that organizes files in a directory into folders based on file type. 
    For example, all .txt files go into a "Text Files" folder, all .jpg and .png files go into an "Images" folder, and so on.

How the Project Works
    Here are what the script should do step by step:
    Use glob to Find Files:
        Use the glob module to find all files in the target directory with specific patterns (like *.txt for text files).
    Create Folders Based on File Type:
        For each file type, create a corresponding folder (e.g., "Text Files", "Images").
    Move Files to the Appropriate Folder:
        Move the files into the appropriate folder based on their extension using shutil.move().
'''


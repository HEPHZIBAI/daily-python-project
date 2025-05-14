'''
Project Brief
    Your task for this project is to merge text files using Python.

Project Instructions
    Download and extract these text files and place them in a folder.
    Write a program that:
        Reads the content of each text file
        Merges the content/string of each file making sure the content of a.txt comes first, then b.txt, then c.txt.
        Writes the merged string into one single text file.

Project Expected Output
    The expected output is a generated merged_file.txt file that contains the content of all three input files.
'''
with open("./real world project./3.Merge text files/merge.txt",'a') as f:

    with open("./real world project./3.Merge text files/a.txt",'r') as a:
        for i in a.readlines():
            f.write(i+"\n")

    with open("./real world project./3.Merge text files/b.txt",'r') as a:
        for i in a.readlines():
            f.write(i+"\n")

    with open("./real world project./3.Merge text files/c.txt",'r') as a:
        for i in a.readlines():
            f.write(i+"\n")
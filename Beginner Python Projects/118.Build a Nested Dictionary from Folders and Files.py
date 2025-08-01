'''

Your task for today is to write a Python program that scans folders representing classes (like "math", "science", etc.), reads all the .txt files in each folder, and builds a nested dictionary containing the file contents. This project will help you practice working with folders, files, and nested data structures — all very common in real-world automation and data collection.

📝 Project Task
The program should:

Start with a main folder (e.g. students/), where each subfolder represents a subject (math/, science/, etc.).

Inside each subject folder, there are text files for each student (alice.txt, bob.txt, etc.).

Read the content of each file.

Build a dictionary that looks like this:

{
  "math": {
    "alice.txt": "Alice's math notes here",
    "bob.txt": "Bob's math notes here"
  },
  "science": {
    "alice.txt": "Alice's science notes here"
  }
}
This is a very useful pattern for gathering, organizing, and transforming text data from folders into structured Python dictionaries.

📌 Expected Output
The output should be a dictionary where each key is a folder name (like math, science) and each value is another dictionary mapping filenames to their content.

For example, given this structure:

students/
├── math/
│   ├── alice.txt
│   └── bob.txt
├── science/
│   └── alice.txt
Your program should output something like:

{
  "math": {
    "alice.txt": "I love calculus.",
    "bob.txt": "Geometry is fun."
  },
  "science": {
    "alice.txt": "Physics is fascinating."
  }
}


'''
'''
Project Overview 💡
    In this project, you'll build a simple text analyzer in Python. 
    You'll learn how to process text, count words, sentences, and characters, and identify the most frequent word. 
    This is a great exercise in string manipulation and working with dictionaries.

Task:
    Write a Python script that takes a user-inputted block of text and analyzes it by calculating the number of characters, words, and sentences. 
    Additionally, determine the most frequently used word and calculate the average word and sentence length.

Expected Output:
    The program should output text statistics, including:
    Total Characters
    Total Words
    Total Sentences
    Most Frequent Word
    Average Word Length
    Average Sentence Length

you can use text:
    Trees usually reproduce using seeds. Flowering plants have their seeds inside fruits, while conifers carry their seeds in cones, and tree ferns produce spores instead.
'''

sent=input("enter a block of text for analysis:\n").strip().lower()
s=" "+sent[::]+" "
avg=0
word="   "
punctuation = ".,!?:;'\"()[]{}"
for char in punctuation:
    s = s.replace(char, "")

for i in list(set(s.split())):
    avg+=(len(i)*(s.count(i)))
    i=' '+i+' '

    if s.count(i)>s.count(word):
        word=i



print("text analysis results: ")

print("total characters:",len(sent))
print("total words:",len(sent.split()))
print("total sentence:",sent.count('.')+sent.count('!')+sent.count('?'))
print("most frequent word:\'",word,"\' (used",s.count(word),"times)")
print("average word length:",avg/len(sent.split()),"characters")
print("average sentence length:")



'''
# Step 1: Get user input
text = input("Enter a block of text for analysis:\n")

# Step 2: Initialize counters and storage
character_count = len(text)
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')
word_frequency = {}

# Step 3: Define a function to remove punctuation
def remove_punctuation(s):
    punctuation = ".,!?:;'\"()[]{}"
    for char in punctuation:
        s = s.replace(char, "")
    return s

# Step 4: Analyze the text
cleaned_text = remove_punctuation(text).lower()
words = cleaned_text.split()

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Step 5: Calculate additional statistics
if word_count > 0:
    most_frequent_word = max(word_frequency, key=word_frequency.get)
    average_word_length = sum(len(word) for word in words) / word_count
    average_sentence_length = word_count / sentence_count if sentence_count > 0 else word_count
else:
    most_frequent_word = None
    average_word_length = 0
    average_sentence_length = 0

# Step 6: Display the results
print("\nText Analysis Results:")
print("-" * 22)
print(f"Total Characters: {character_count}")
print(f"Total Words: {word_count}")
print(f"Total Sentences: {sentence_count}")

if most_frequent_word:
    print(f"Most Frequent Word: '{most_frequent_word}' (used {word_frequency[most_frequent_word]} times)")

print(f"Average Word Length: {average_word_length:.2f} characters")
print(f"Average Sentence Length: {average_sentence_length:.2f} words")
'''
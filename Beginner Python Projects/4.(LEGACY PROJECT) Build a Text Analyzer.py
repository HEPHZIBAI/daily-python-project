'''
Project Description
    This program takes a block of text provided by the user, analyzes it, and provides useful statistics about the text to the user.

How the Project Works
    The program starts by prompting the user to enter some text in the terminal:
    The user pastes some text.
    After the user presses Enter, they get different statistics about the submitted text: 
    the number of words, sentences, and characters, the most frequent words used in the text, the average word length, and the average sentence length.

sample text:
    Common frogs metamorphose through three disti nct developmental life stages aquatic larva , terrestrial juvenile, and adult. 
    They have corpulent bodies with a rounded snout, webbed feet and long hind legs adapted for swimming in water and hopping on land. 
    Corfimon frogs ar e often confused with the common toad (Bufo b ufo), but frogs can easily be distinguished a s they have longer legs, hop, and have a mois t skin, whereas toads crawl and have a dry 'w arty' skin. 
    The spawn of the two species also differs, in that frog spawn is laid in clumps and toad spawn is laid in long strings.
'''

sentence=input("enter a block of text for analysis: ").strip()
l=0
print("text analysis results:\n-------------------------------")
print("total characters:",len(sentence)-sentence.count(' '))
print("total words:",len(sentence.split()))
print("total sentences:",sentence.count('.'))
print(f"most frequent word: '{0}' (used {0} times)")
print("average word length:",l,"characters")
print("average sentence length:",l,"words")
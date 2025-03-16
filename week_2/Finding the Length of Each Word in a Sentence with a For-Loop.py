sentence = "The weather is good"
length=[]
for i in sentence.split():
    length.append(len(i))

print(sentence,sentence.split(),length,sep='\n')
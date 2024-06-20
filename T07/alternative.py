
sentence=str(input("Enter a Sentence: "))

# Splits the sentenc where there are spaces so each element is a word of the sentence
sentenceListWord=sentence.split(" ")

# Splits the sentences after every character
sentenceListChar=list(sentence)

counterWord=0
counterChar=0

# Goes through the list where every even postion of the list gets changed to lower case and the odd to upper case
for i in sentenceListWord:

    if counterWord % 2 ==0:
        sentenceListWord[counterWord]=i.lower()
    else:
        sentenceListWord[counterWord]=i.upper()
    counterWord += 1

#Turns the list back into a string joining them with a space between each element of the list
finalSentenceWord=" ".join(sentenceListWord)
print(finalSentenceWord)


# Goes through the list where every even postion of the list gets changed to upper case and the odd to lower case
for i in sentenceListChar:
    if counterChar % 2 ==0:
        sentenceListChar[counterChar]=i.upper()
        
    else:
        sentenceListChar[counterChar]=i.lower()
        
    counterChar += 1
    

#Turns the list back into a string joining them with nothing between each element of the list
finalSentenceChar="".join(sentenceListChar)
print(finalSentenceChar)

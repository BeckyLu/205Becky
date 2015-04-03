import urllib
import wikipedia
import bs4

file = open("stop-words.txt")
stopwords = file.readlines()

for word in stopwords:
    next = word.strip()
    print(next)

def removeStopwords(removeWord):
    
    for stopword in stopwords:
        removeWord = removeWord.replace(" " + stopword.strip() + " ", " ")
        #print removeWord        #Debugging
    return removeWord
    

while True:
    inputString = raw_input("Greetings! Who are you? ")
    filtered = removeStopwords(inputString)
    
    print filtered            #Debugging
    print inputString         #Debugging
    
    print("Hello there " + filtered)
#else:
    
    
    
    #filtered = input.replace(" ni ", " <beep> ")
    #print("Your filtered text was: " + filtered)
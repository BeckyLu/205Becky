import urllib
import wikipedia
import bs4

file = open("stop-words.txt")
stopwords = file.readlines()

#for word in stopwords:
#    next = word.strip()
    #print(next)

def removeStopwords(removeWord):  
    for stopword in stopwords:
        message = stopword.strip()
        removeWord = removeWord.replace(" " + message + " ", " ")
        #print removeWord        #Debugging
    return removeWord
    

inputString = raw_input("Greetings! Who are you? ")
inputString = " " + inputString + " "
name = removeStopwords(inputString)
print("Hello " + name.strip() + " How're you today?")
    #filtered = removeStopwords(inputString)
    
    #print filtered            #Debugging
    #print inputString         #Debugging
    
    #print("Hello there " + filtered + " How're you today?")
#else:
    
    
    
    #filtered = input.replace(" ni ", " <beep> ")
    #print("Your filtered text was: " + filtered)
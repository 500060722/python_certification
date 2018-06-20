'''
Created on Jun 19, 2018

@author: Prajjawal Banati
'''
import random

def check_length(key):
    if len(key)>3:
        return True
    elif len(key)==3:
        return False
    else:
        return False
def check_punctuation(key):
    global correct
    correct=key
    global a
    a=[",",".","'"]
    if a[0] in key:
        key=key.replace(",","")
    if a[1] in key:
        key=key.replace(".","")
    if a[2] in key:
        key=key.replace("'","")
    return key
def scramble(word):
    char1 = random.randint(1, len(word)-2)
    char2 = random.randint(1, len(word)-2)
    while char1 == char2:
        char2 = random.randint(1, len(word)-2)
    newWord = ""
    for i in range(len(word)):
        if i == char1:
            newWord = newWord + word[char2]
        elif i == char2:
            newWord = newWord + word[char1]
        else:
            newWord = newWord + word[i]
    
    b=len(newWord)
    if len(correct)>len(newWord):
        if a[0] in correct:
            newWord=newWord+a[0]
        if a[1] in correct:
            newWord=newWord+a[1]
        if a[2] in correct:
            newWord=newWord[0:(len(newWord)-1)]+a[2]+newWord[b-1]
    return newWord        
  


    
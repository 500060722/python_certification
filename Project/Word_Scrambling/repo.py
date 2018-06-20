'''
Created on Jun 19, 2018

@author: Prajjawal Banati
'''
from main import check_length
from main import check_punctuation
from main import scramble
c=""
string=""
def jumbled(key):
    global string
    string=string+" "+key    

file=open("C:\\Users\\Prajjawal Banati\\Desktop\\Assignments\\Module_1\\Testfile1.txt","r")
print("The string before scrambling is:")
for line in file:
    print(line)
    List=line.split()
for token in List:
    a=check_length(token)
    if a==True:
        b=check_punctuation(token)
        b=scramble(b)
        jumbled(b)
    else:
        jumbled(token)
print("The string after scrambling is:\n{}".format(string))
    

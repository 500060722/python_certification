print("Hello Everyone! The following program will take two string as an input \
from your and will concatenate all the capital letters from both the strings")
#Storing a string of capital letters in compiler to compare it with strings 1 and 2
default="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#Storing two Empty strings in which we insert the capital letter string
capital_string_1=""
capital_string_2=""
#Store length 
a=len(default)
string_1 = input("Enter string 1: ")
b=len(string_1)
#Comparing each letter of string with the alphabet string
for i in range(0,b,1):
    for j in range(0,a,1):
        if string_1[i]==default[j]:
            capital_string_1 = capital_string_1 + string_1[i]                     
print("The capital string in string_1 is",capital_string_1)
string_2 = input("Enter string 2: ")
b=len(string_2)
for i in range(0,b,1):
    for j in range (0,a,1):
        '''If the element gets equal to any alphabet in default string it will get
            stored in the empty capital_string_2'''
        if string_2[i]==default[j]:
            capital_string_2 = capital_string_2 + string_2[i]
            
print("The capital string in string_2 is:",capital_string_2)
print("So the concatenated string is:",capital_string_1 + capital_string_2)

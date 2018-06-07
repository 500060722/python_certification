print("Hello Everyone! This is the program of checking whether \
the strings are palindrome or not")
string=input("Input the string: ")
print("The original string is:",string)
#using an empty string to concatenate it while reversing
reverse_string=""
a=len(string)
#Reversing the string using a for loop
for i in range(-1,-a-1,-1):
    #See here "b" will start storing the reverse string
    reverse_string=reverse_string+string[i]
print("The string after reversing will be:",reverse_string)
if string==reverse_string:
    print("The string is in palindrome")
else:
    print("The strings is not in palindrome")
    
    

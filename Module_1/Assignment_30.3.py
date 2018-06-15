print("Hello Everyone! This is the program of checking whether the string is \
palindrome or not")
string=input("Input the string: ")
print("The original string is:",string)
a=len(string)
concatenated=""
b=a-1
def reverse_string(b,string):
    global concatenated
    if b<0:
        return
    else:
        concatenated=concatenated+string[b]
        b=b-1
        reverse_string(b,string)
    return concatenated
    
reverse_string=reverse_string(b,string)
print(reverse_string)
if reverse_string==string:
    print("Both strings are in Palindrome")
else:
    print("The strings are not in palindrome")

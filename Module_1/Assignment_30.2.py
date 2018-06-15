print("Hello Everyone! This is the program of printing the reverse string")
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

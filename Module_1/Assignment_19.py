print("Hello Everyone the following program will take a string from you \
then it would select only the even places of the string ignoring the spaces \
and will give you a string in the reversed order")
resultant_string=""
expected_output=""
accepted_string = input("Write a string: ")
print(accepted_string)
#replace funtion is used to replace any variable or a space in the string
#So here we replaced the spaces to get the correct position of string
accepted_string=accepted_string.replace(" ","")
a=len(accepted_string)
for i in range(0,a,1):
    if (i%2==0):
        resultant_string=resultant_string+accepted_string[i]
        
print("The resultant_string of the accepted_string will be:",resultant_string)
b=len(resultant_string)
for i in range(b-1,-1,-1):
    expected_output=expected_output+resultant_string[i]
print("The expected_output of the string will be:",expected_output)

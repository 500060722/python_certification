print("Hello Everyone this is the program to check whether a number is prime or not")
print("So to begin with input the number which you want to find whether it is prime or not")
num=int(input("Enter the number: "))
if num<=1:
    print(num,"is not a prime number")
else:
    for value in range(2,num):
        if num%value==0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
            break
    

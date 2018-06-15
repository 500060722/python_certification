print("FIBONACCI SERIES PROGRAM:")
print("This program will print fibonacci series using recursion:\n")
number=int(input("Enter the number limit till you want to print series: "))
def FIBO(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return FIBO(number-1)+FIBO(number-2)
ans=FIBO(number)
print(ans)

print("The following program will print the multiples of 3 using recursion")
n=int(input("Enter the value of n: "))
multiple=[]
def multiples(n):
    if n==1:
        return multiple.append(3)
    else:
        multiple.append(n*3)
        n-=1
        return multiples(n)
multiples(n)
print(multiple[::-1])

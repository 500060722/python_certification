print("Hello Everyone, This program will print the sum of all the numbers from 1 to n \
(User will input the value of n)")
n=int(input("Enter the value of n: "))
def sum(n):
    print("So the sum of natural numbers from 1 to",n,"is: ")
    k=0
    for value in range(1,n+1):
        k=k+value
    print(k)
sum(n)
        

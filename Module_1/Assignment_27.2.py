print("FIBONACCI SERIES PROGRAM")
num=int(input("Enter the limit untill you want to print fibonacci series: "))
def fibonacci(num):
    first_term=0
    second_term=1
    for value in range(1,num):
        print(first_term)
        next_term=first_term+second_term
        first_term=second_term
        second_term=next_term
fibonacci(num)    

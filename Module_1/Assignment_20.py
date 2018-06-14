print("Fibonacci numbers in a list:")
print("Print the fibonacci series in a list.")
num=int(input("Enter the limit untill you want to print fibonacci series: "))
fibonacci_list =[]
first_term=0
second_term=1
for i in range(0,num):
    fibonacci_list.insert(i,first_term)
    next_term=first_term+second_term
    first_term=second_term
    second_term=next_term

print("The fibonacci series list till limit",num,"is:")
print (fibonacci_list)


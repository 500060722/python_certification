print("Hello the following program will print the even numbers between \
50 and 80 using 'for' loop")
ch=input("So,Shall we start(y|n): ")
if ch=="y":
    for value in range(49,81):
        if value%2==0:
            print(value)
elif ch=="n":
    print("Please press y key on the keyboard to run the program")
else:
    print("Wrong! Input Please Try Again!!!!!")
    

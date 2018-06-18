try:
    myList=["1","2","3","4","5"]
    sum=0
    for i in myList:
        sum=sum+int(i)
    print(sum)
    print(myList[4])

except SyntaxError:
    print("There is a syntax error in the following program")
except IndexError:
    print("The index is out of range")
except TypeError:
    print("There is a type error in the above program")


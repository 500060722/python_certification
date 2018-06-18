List=[]
import random
print("Randomly printed numbers are:\n")
for i in range(1,11):
    a=random.randint(1,10)*100
    List.insert(i,a)
print(List)

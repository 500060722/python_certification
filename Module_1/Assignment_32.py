file=open("D:\\courses\\courses.txt","r")
List=[]
for line in file:
    tokens=line.split()
    List=List+tokens
print("List represntation of the courses are:",List)
Dictionary={}
for i in range(len(List)):
    Dictionary[i]=List[i]
print("The dictionary representation of the course are",Dictionary)

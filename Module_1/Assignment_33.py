file=open("D:\\courses\\Student_Details.txt","r")
List=[]
Dictionary={}
for line in file:
    tokens=line.split()
    List=List+tokens
print("The list represenation of the rollno and mame is",List)
for i in range(1,len(List),2):
    key=List[i-1]
    Dictionary[key]=List[i]
    i=i+1
print("The dictionary representation is",Dictionary)
    

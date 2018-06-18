file=open("D:\\courses\\rhyme.txt","r")
for line in file:
    tokens=line.split()
    print("Wordcount:"+str(len(tokens))+" In line:",line)

TestFile1=open("C:\\Users\\Prajjawal Banati\\Desktop\\Assignments\\Module_1\\TestFile1.txt","w")
TestFile1.write('"Hello Pune"')
TestFile1.close()
TestFile1=open("C:\\Users\\Prajjawal Banati\\Desktop\\Assignments\\Module_1\\TestFile1.txt","r+")
TestFile2=open("C:\\Users\\Prajjawal Banati\\Desktop\\Assignments\\Module_1\\TestFile2.txt","w")
for line in TestFile1:
    line.split(' ')
    TestFile2.write('\\'+line+'\\')
        
TestFile2.close()
TestFile1.close()


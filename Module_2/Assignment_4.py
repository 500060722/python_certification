import cx_Oracle
con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
cur=con.cursor()
cur.execute(""" create table Vehicles(Vehicleid number(5) primary key,vehiclename varchar2(10))""")
print("Table created Successfully")
counter=2000
cur.executemany("INSERT INTO Vehicles values(:1 , :2)",[(counter+1,'Toyota'),(counter+2,'Maruti'),(counter+3,'Nissan'),(counter+4,'Hyundai')])
print("Values inserted successfuly using positonal bind variables. The values are: ")
cur.execute("select * from Vehicles")
for line in cur:
    print(line)
cur.executemany("INSERT INTO Vehicles values(:vehicleid,:vehiclename)",
                [{'vehicleid':counter+6,'vehiclename':'Honda'},
                 {'vehicleid':counter+7,'vehiclename':'Volkswagen'}])
print("Values inserted successfully using named bind variables. Now All the values are: ")
cur.execute("select * from Vehicles")
for line in cur:
    print(line)
con.commit();
cur.close()
con.close()

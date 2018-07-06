import cx_Oracle
con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
cur=con.cursor()
print("Before Update operation we have the following rows: ")
cur.execute("Select * from Vehicles")
for line in cur:
    print(line)
counter=1000
cur.execute("Select Vehiclename from Vehicles")
cur.execute("update Vehicles set Vehicleid = :vehicle where Vehiclename = :name",{'vehicle':counter+1,'name':'Toyota'})
cur.execute("update Vehicles set Vehicleid = :vehicle where Vehiclename = :name",{'vehicle':counter+2,'name':'Maruti'})
cur.execute("update Vehicles set Vehicleid = :vehicle where Vehiclename = :name",{'vehicle':counter+3,'name':'Nissan'})
cur.execute("update Vehicles set Vehicleid = :vehicle where Vehiclename = :name",{'vehicle':counter+4,'name':'Hyundai'})
cur.execute("update Vehicles set Vehicleid = :vehicle where Vehiclename = :name",{'vehicle':counter+6,'name':'Honda'})
cur.execute("update Vehicles set Vehicleid = :vehicle where Vehiclename = :name",{'vehicle':counter+7,'name':'Volkswagen'})
print("After Updating the 'vehicleid' we have following rows: ")
cur.execute("Select * from Vehicles")
for line in cur:
    print(line)
cur.execute("update Vehicles set Vehiclename = :name where Vehicleid = :vehicleid",{'vehicleid':counter+3,'name':'Mahindra'})
print("After Updating the name as 'mahindra' we have following rows: ")
cur.execute("Select * from Vehicles")
for line in cur:
    print(line)    
con.commit()
cur.close()
con.close()

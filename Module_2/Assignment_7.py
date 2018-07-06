import cx_Oracle
con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
print("Deleting the data of user with user id 1 we have: ")
cur=con.cursor()
Id=1
cur.execute("delete from Users where Userid = :ID",{'ID':Id})
cur.execute("Select * from Users")
for line in cur:
    print(line)
print("Coming On to Next Question. Delete a record from 'Vehicle' table using named bind variables. Accept VehicleId as an input from the user.")
vehicleid = input("enter the vehicle id of the car which you want to delete: ")
cur.execute("delete from Vehicles where Vehicleid = :ID",{'ID':vehicleid})
cur.execute("Select * from Vehicles")
for line in cur:
    print(line)
con.commit()
cur.close()
con.close()

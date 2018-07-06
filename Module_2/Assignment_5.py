import cx_Oracle
con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
cur=con.cursor()
ID=4
user_name="lookingfojob@yahoo.com"
user_type="Jobseeker"
print("Before Update operation we have the following row: ")
cur.execute("Select * from Users where Userid = :ID",{'ID':ID})
for line in cur:
    print(line)
cur.execute("""update Users set Username = :name , Usertype = :type where Userid = :ID""",{'name':user_name,'type':user_type,'ID':ID})
print("After updating we have: ")
cur.execute("Select * from Users where Userid = :ID",{'ID':ID})
for line in cur:
    print(line)
ID=1
password=input("Enter the new password for User 1.")
print("Before Update the password of the User1 is:")
cur.execute("Select Password from Users where Userid = :ID",{'ID':ID})
for line in cur:
    print(line)
cur.execute("""update Users set Password = :password where Userid = :ID""",{'password': password,'ID':ID})
print("After updating we have: ")
cur.execute("Select Password from Users where Userid = :ID",{'ID':ID})
for line in cur:
    print(line)
con.commit()
cur.close()
con.close()

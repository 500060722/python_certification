import cx_Oracle
con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
cur=con.cursor()
cur.execute(""" create table Users(Userid number(10) primary key check(length(userid)>=1),Username varchar2(30) not null,Password varchar2(20) not null,Usertype varchar2(20) check (usertype in ('Employer','Jobseeker')))""")
print("Table created successfully")
user_id=2
user_name="careers@accenture.com"
password="Acc1"
user_type="Employer"
user_id_1=3
user_name_1="rahulitsme@gmail.com"
password_1="rahulindia93"
user_type_1="Jobseeker"
user_id_2=4
user_name_2=input("Enter the name of the user: ")
password_2=input("Enter the password of the 4th user: ")
user_type_2=input("Enter whether he is employer or Jobseeker: ")
cur.execute("Insert into Users values(1,'jobs@infosys.com','jobs@infosys','Employer')")
cur.execute("""Insert into Users values(:ID, :name, :password, :usertype)""",{'ID' : user_id,'name' : user_name,'password' : password,'usertype' : user_type})
cur.execute("Insert into Users values(:u1,:u2,:u3,:u4)",(user_id_1,user_name_1,password_1,user_type_1))
cur.execute("""Insert into Users values(:ID, :name, :password, :usertype)""",{'ID' : user_id_2,'name' : user_name_2,'password' : password_2,'usertype' : user_type_2})
print("Values Inserted Successfully")
con.commit()
cur.close()
con.close()

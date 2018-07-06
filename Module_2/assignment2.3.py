import cx_Oracle
city=input("Enter Name of City: ")
con = cx_Oracle.connect('SYSTEM/user123@localhost/xe')
cur = con.cursor()
cur.execute(""" SELECT CompanyName,Mobile,EmailId from Employer where RenewalStatus =:param1 AND city =:param2 """,(city,'Active'))
res = cur.fetchall()
print(res)
con.close()

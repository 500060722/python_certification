import cx_Oracle
city=input("Enter the name of city: ")
con = cx_Oracle.connect('SYSTEM/user123@localhost/xe')
cur = con.cursor()
cur.execute(""" SELECT CompanyName,Mobile,EmailId from Employer where RenewalStatus =:param1 AND city =:param2 """,{'param1':'Active','param2':city})
res = cur.fetchall()
print(res)
con.close()

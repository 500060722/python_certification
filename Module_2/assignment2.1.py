import cx_Oracle
con = cx_Oracle.connect('SYSTEM/user123@localhost/xe')
cur = con.cursor()
cur.execute(""" SELECT CompanyName,EmailId from Employer where IndustryType = 'IT' AND City = 'Bangalore' """)
res = cur.fetchall()
print(res)
con.close()

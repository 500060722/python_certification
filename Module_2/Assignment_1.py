import cx_Oracle
con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
cur=con.cursor()
cur.execute('Select * from Employer')
for line in cur:
    print(line)
cur.execute("Select * from Employer")
print("After fetchall the row count is:",cur.rowcount)
cur.close()
con.close()

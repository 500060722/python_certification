try:
    import cx_Oracle
    con=cx_Oracle.connect("SYSTEM/ser123@localhost/xe")
    cur=con.cursor()
    Id=2
    cur.execute("delete from Users where User_id = :ID",{'ID':Id})
    cur.execute("Select * from Users")
    for line in cur:
        print(line)
except cx_Oracle.DatabaseError as e:
    print("There is error in the following program.")
    print("The error is as follows:",e)
else:
    print("In final block")
    con.close()


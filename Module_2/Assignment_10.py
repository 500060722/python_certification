try:
    import cx_Oracle
    con=cx_Oracle.connect('SYSTEM/user123@localhost/xe')
    cur=con.cursor()
    cur.execute("INSERT INTO product VALUES('P106','Jams','150','10')")
    con.close()
except cx_Oracle.DatabaseError as e:
    print("There is error in the above program. That is as follows:")
    print(e)
else:
    print("Values Written successfully........")

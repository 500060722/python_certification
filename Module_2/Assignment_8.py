import cx_Oracle
con=cx_Oracle.connect('SYSTEM/user123@localhost/xe')
cur=con.cursor()
print("Creating Table..........")
cur.execute("""create table Account(Customerid number(5) , Accountno varchar2(15) , Accounttype varchar2(10) , Balance number(10))""")
print("Table created Successflly...........")
counter = 100
bal=0
print("Insering values into the table.......")
cur.executemany("INSERT INTO Account values(:customerid,:accountno,:accounttype,:balance)",
                [{'customerid':counter+1 , 'accountno':'IBI1001' , 'accounttype':'Savings' , 'balance': bal},
                 {'customerid':counter+2 , 'accountno':'IBI1002' , 'accounttype':'Current' , 'balance': bal+1200},
                 {'customerid':counter+3 , 'accountno':'IBI1003' , 'accounttype':'Savings' , 'balance': bal+6543},
                 {'customerid':counter+4 , 'accountno':'IBI1004' , 'accounttype':'Recurring','balance': bal+7500},
                 {'customerid':counter+5 , 'accountno':'IBI1005' , 'accounttype':'Current' , 'balance': bal}])
print("5 Values Inserted Successfully........That are the values:")
cur.execute("select * from Account")
for line in cur:
    print(line)
print("2. The customerid and balance of the cutomer with maximum balance is:")
cur.execute("select Customerid , Balance from Account where Balance = 7500")
for line in cur:
    print(line)
print("3. (BEFORE UPDATE)The balance of the account of the customer with customer id = 102 is:")
Id = 102
cur.execute("select Balance from Account where Customerid = :id",{'id':Id})
for line in cur:
    acct_bal=line[0]
print(acct_bal)
acct_bal=acct_bal+2000
print("4. The amount after incrementing balance by 2000 of customerid of 102 is:")
print(acct_bal)
print("Updating this balance........")
cur.execute("update Account set Balance = :balance where Customerid = :id",{'balance':acct_bal,'id':Id})
print("Done........Now the credentials(AFTER UPDATE) of 102 is:")
cur.execute("select * from Account where Customerid = :id",{'id':Id})
for line in cur:
    print(line)
print("5. Deleting the account no. of zero balances we have:")
counter = 0
cur.execute("delete Account where Balance = :zero",{'zero':counter})
cur.execute("select * from Account")
for line in cur:
    print(line)
con.commit()
cur.close()
con.close()


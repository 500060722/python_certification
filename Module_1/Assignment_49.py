student_tuples=[('John','A',15),('Jane','B',12),('Dave','B',10)]
print(sorted(student_tuples,key=lambda student : student[2]))
print(sorted(student_tuples,key=lambda student : student[2],reverse=True))

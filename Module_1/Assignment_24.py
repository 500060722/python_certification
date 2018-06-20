python_marks={"John": 86.5,"Jack": 91.2,"Jill": 84.2,"Harry": 72.1,"Joe": 80.5}
print(python_marks)
descending_list=sorted(python_marks.values(),reverse=True)
print("The top two scorers of the class are:\n")
for key in descending_list:
    print(key)
    python_marks[key]

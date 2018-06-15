java_course={"John","Jack","Jill","Joe"}
python_course={"Jake","John","Eric","Jill"}
print("The students who are a part of Python course are:\n",python_course)
print("The students who are a part of Java Course are:\n",java_course)
print("The students who are only a part of python course:\n",python_course-java_course)
print("The students who are a part of both courses are:\n",python_course&java_course)
print("The students who are a part of Either Java or Python courses but not both:\n",
      (python_course|java_course)-(python_course&java_course))
print("The students who are part of either python course or java course are:\n",
      python_course|java_course)

python_students = {"Nikhil", "Rehan", "Nisarg", "Siddhant"}
java_students = {"Nisarg", "Siddhant", "Rehan", "Shubham"}

print("Students in both courses:", python_students & java_students)

single = python_students ^ java_students

print("Students enrolled in only one course:", single)
import numpy as np
marks = np.array([65, 78, 45, 90, 55, 82, 70, 60, 88, 50,
                  72, 95, 40, 68, 85, 58, 76, 92, 62, 80])

average = np.mean(marks)

print("Marks:")
print(marks)
print("Class average:", average)
print("Marks above average:")
print(marks[marks > average])
import matplotlib.pyplot as plt
marks = list(map(int, input("Enter marks: ").split()))
plt.hist(marks, bins=5, edgecolor='black')
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.title("Marks Distribution")
plt.show()
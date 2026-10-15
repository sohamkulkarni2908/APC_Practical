import matplotlib.pyplot as plt
names = input("Enter names: ").split()
marks = list(map(int, input("Enter marks: ").split()))
plt.barh(names, marks)
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.title("Marks Comparison")
plt.show()
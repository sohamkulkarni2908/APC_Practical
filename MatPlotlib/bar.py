import matplotlib.pyplot as plt
names = input("Enter names: ").split()
marks = list(map(int, input("Enter marks: ").split()))
plt.bar(names, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks Comparison")
plt.show()
import matplotlib.pyplot as plt
labels = input("Enter categories: ").split()
values = list(map(int, input("Enter values: ").split()))
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
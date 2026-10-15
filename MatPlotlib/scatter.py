import matplotlib.pyplot as plt
x = list(map(int, input("Enter x values: ").split()))
y = list(map(int, input("Enter y values: ").split()))
plt.scatter(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot")
plt.show()
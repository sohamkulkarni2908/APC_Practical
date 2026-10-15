import matplotlib.pyplot as plt
x = list(map(int, input("Enter x values: ").split()))
y = list(map(int, input("Enter y values: ").split()))
plt.plot(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Graph")
plt.show()